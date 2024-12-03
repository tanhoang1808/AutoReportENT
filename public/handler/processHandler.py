from datetime import datetime
from handler import facebookHandler
from config import facebook
from handler import worksheetHandler
import contraints


def process_employee_data(employee, data, employee_data):
    access_token = facebook.get_access_token()
    print("data[client-url]",data["client_url"])
    if data["client_url"]:
        facebook_data = facebookHandler.get_facebook_data(data["client_url"], access_token)
        service_account_file = "service_account.json"
        weekly_info = facebookHandler.get_data_from_json(facebook_data,employee)

        #Neu nhu lay du lieu thanh cong tu Facebook thi bat dau update du lieu
        if weekly_info:
            new_sheet_url = ""
            now = datetime.now()
            month = now.strftime("%m")
            current_month = "Tháng " + month #Title Worksheet
            current_year = str(datetime.now().year)
            year_folders = contraints.get_year_folder()
            month_folders = contraints.get_month_folder(current_year)
            year_folder_id = year_folders.get(current_year)
            folder_id = month_folders.get(current_month).format(year_folder_id)
            
            if current_year not in employee_data[employee]["sheet_url"]:
                # Nếu chưa có báo cáo thì tạo ( Facebook)
                employee_data[employee]["sheet_url"][current_year]["Facebook"] = {}
            if current_month not in employee_data[employee]["sheet_url"][current_year]["Facebook"]:
                new_sheet_url = worksheetHandler.create_new_google_sheet(employee, 
                                                                         current_month, current_year,
                                                                        folder_id, 
                                                                        weekly_info,
                                                                        )
                print("new_sheet_url :",new_sheet_url)
                if new_sheet_url is None:
                    return
                employee_data[employee]["sheet_url"][current_year]["Facebook"][current_month] = new_sheet_url
                worksheetHandler.update_google_sheets(new_sheet_url, weekly_info, employee_data[employee]["channel"])
            else:
                new_sheet_url = employee_data[employee]["sheet_url"][current_year]["Facebook"][current_month]
                worksheetHandler.update_google_sheets(new_sheet_url, weekly_info, employee_data[employee]["channel"])
    
        else:
            print(f"Failed to get data for employee {employee}, maybe the accound id has terminated.")
    else:
        print(f"employee {employee} not have client_url")
        return -1
