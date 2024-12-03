import sys
import authorize
import contraints
import gspread
import time
from googleapiclient.errors import HttpError
CAMPAIGN_INFO = contraints.CAMPAIGN_INFO
from googleapiclient.discovery import build
from handler import worksheetDecor






def set_default_campaign():
    default_campaigns = contraints.DEFAULT_CAMPAIGN
    return default_campaigns


def create_hard_table_range(hard_table_data,worksheet,_current_month):
    default_hard_table = hard_table_data
        # Create hard table_range
        #  Các sản phẩm mặc định trong báo cáo
    default_campaigns = set_default_campaign()

        # Thêm các chiến dịch mặc định vào hard_table_data nếu chưa tồn tại
    for campaign_name, campaign_info in default_campaigns.items():
        campaign_found = False
        for date, camp_data in sorted(default_hard_table.items()):
            if campaign_name in camp_data:
                campaign_found = True
                break
        if not campaign_found:
                default_hard_table.setdefault(_current_month, {}).setdefault(campaign_name, {
                    "total_spend": campaign_info["total_spend"],
                    "date_stop": campaign_info["date_stop"]
                })
    print("default_hard_table :",default_hard_table)
     
        # Các dòng dữ liệu cho bảng hard table
    campaign_data = []
    range_title_table = "C1"
    worksheet.update([["Ngân Sách".upper(), "SP/DV".upper(), "Target Lead".upper(), "Lead thực nhận".upper(),
                           "Còn lại".upper(), "Tỷ lệ hoàn thành".upper(),
                           "Chi tiêu".upper(), "CPL".upper(), "Ngân sách còn".upper(), "Target CPL".upper(),
                           "Điểm KPI CPL".upper(), "Điểm KPI LEAD".upper()]], range_name="C1")

    end_row = 2
    for date, camp_data in default_hard_table.items():
        print(f"Processing date: {date}, camp_data: {camp_data}")  # In kiểm tra dữ liệu
        for camp_group, spend_info in camp_data.items():
            print("campgroup :",camp_group)
            
    
            info = CAMPAIGN_INFO.get(camp_group, {
                    "budget": 0,
                    "target_cpl": 0,
                    "target_lead": 0,
                    "coefficient": 0
                })

            budget = info["budget"]
            target_cpl = info["target_cpl"]
            target_lead = info["target_lead"]
            coefficient = info["coefficient"]
            course = camp_group

            total_spend_formula = f"=SUMIF(D13:D,\"{course}\",G13:G)"
            row = [
                    budget,
                    camp_group,
                    target_lead,
                    f"=SUMIF(D13:D,\"{camp_group}\",E13:E)",
                    "=E{}-F{}".format(end_row, end_row),  # công thức cho cột "Còn lại"
                    "=IFERROR(F{}/E{} * 100%,0)".format(end_row, end_row),  # công thức cho cột "Tỷ lệ hoàn thành"
                    total_spend_formula,
                    "=IFERROR(I{}/F{},0)".format(end_row, end_row),
                    "=C10-I10",
                    target_cpl,
                    "=IFERROR((L{}/J{}) * {},0)".format(end_row, end_row, coefficient),
                    "=IFERROR((F{}/E{}) * {},0)".format(end_row, end_row, coefficient),
                ]
            row_total = [[
                    "=SUM(C2:C9)",
                    "",
                    "=SUM(E2:E9)",
                    "=SUM(F2:F9)",
                    "=SUM(E10-F10)",
                    "=(F10*100%)/E10",
                    "=SUM(I2:I9)",
                    "=SUM(I2:I9)/F10",
                    "=K3",
                    ""

                ]]
            campaign_data.append(row)

            end_row += 1

    if campaign_data:
        worksheet.append_rows(campaign_data, table_range="C2", value_input_option='USER_ENTERED')
        worksheet.append_rows(row_total, table_range="C10", value_input_option="USER_ENTERED")
    # return end_row


def create_new_google_sheet(employee_name, _current_month,_current_year, folder_id, hard_table_data):
    creds,EMAILS = authorize.auth()
    gc = gspread.authorize(creds)
    sheet_title = f"Báo cáo TK Client {_current_month} - {_current_year} - {employee_name}"
    drive_service = build('drive', 'v3', credentials=creds)
    try:
        # Liệt kê ra hết tất cả các sheet của employee
        existing_sheets = gc.list_spreadsheet_files()
        for sheet in existing_sheets:
            if sheet['name'] == sheet_title:
                sheet_id = sheet['id']
                sheet_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}"
                print("sheet with the same name and id has found before create new : ",sheet_url)
                return sheet_url

        
        sheet = gc.create(sheet_title)
        
        sheet_id = sheet.id
       
        file = drive_service.files().get(fileId=sheet_id, fields='parents').execute()

        previous_parents = ",".join(file.get('parents'))
        drive_service.files().update(fileId=sheet_id,
                                     addParents=folder_id,
                                     removeParents=previous_parents,
                                     fields='id, parents').execute()

        sheet_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}"
        print("sheet_url is created :",sheet_url)
        sh = gc.open_by_url(sheet_url)
        worksheet = sh.sheet1
        worksheet.update_title("Facebook")
        for email in EMAILS:
            permission_role = 'writer' if email != 'vi.luong@enternet.edu.vn' else 'reader'
            permission = drive_service.permissions().create(
                fileId=sheet_id,
                body={'type': 'user', 'role': permission_role, 'emailAddress': email, 'sendNotificationEmail': False},
            ).execute()
            
        create_hard_table_range(hard_table_data.copy(),worksheet,_current_month)
        
        # Bat dau format cho defaul table
        # Bat dau o hang 2 vi hang 1 la tieu de
        # Format cho table
        worksheetDecor.formatting_report_table(worksheet,start_row=1,end_row=10)
        worksheetDecor.formatting_data(worksheet)
        if sheet_url is None:
            return -1
        return sheet_url
    except Exception as e:
        print("e")
        print(f"An error occurred in create: {str(e)}")
        return
    except HttpError as e:
        if e.resp.status == 503:
            print("Google Sheet is maintaining....")
        else:
            print(f"An error occurred in create: {str(e)}")
            return


def update_google_sheets(_url, daily_info, channel):
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    creds, _ = authorize.auth()  # Bỏ qua EMAIL vì không cần thiết
    gc = gspread.authorize(creds)

    try:
        sh = gc.open_by_url(_url)
    except HttpError as e:
        if e.resp.status == 503:
            time.sleep(5)
        else:
            print(f"An error occurred in update: {str(e)}")
            return None
    except Exception as e:
        print(f"An error occurred in update: {str(e)}")
        return None

    worksheet = sh.get_worksheet(0)
    worksheet.update(
        [["Thời Gian".upper(), "Kênh".upper(), "Tài Khoản".upper(), "Sản Phẩm/Dịch Vụ".upper(), "Tổng Lead".upper(),
          "Tổng SĐT".upper(), "Chi Tiêu".upper(), "CPL".upper()]],
        range_name="A12")

    client_campaign_data = []
    
    # Lấy dữ liệu của toàn bộ sheet
    all_values = worksheet.get_all_values()
    
    # Lấy hàng cuối cùng
    last_row = len(all_values)
    
    # Bat dau tu hang cuoi + 1
    row_index = last_row + 1
    for date, camp_data in sorted(daily_info.items()):
        for camp_group, spend_info in camp_data.items():
            total_spend = spend_info['total_spend']
            date_stop = spend_info['date_stop']
            account = spend_info["account_name"]
            row = [
                date + " - " + date_stop,
                channel,
                account,
                camp_group,
                "",
                "",
                total_spend,
                "=G{}/E{}".format(row_index, row_index)
            ]
            client_campaign_data.append(row)
            row_index += 1

    if client_campaign_data:
        worksheet.append_rows(client_campaign_data, table_range="A13", value_input_option='USER_ENTERED')
