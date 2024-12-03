from gspread_formatting import *

def formatting_data(_worksheet):
    worksheet = _worksheet
     # Format cho data
        #Format cho cot Chi Tieu
    spend_range = "G13:G"
    cpl_range = "H13:H"
    fmt = {
            "numberFormat": {
                "type": "NUMBER",
                "pattern": "#,##0"
            }
        }
        # Áp dụng định dạng cho các phạm vi
    worksheet.format(spend_range, fmt)
    worksheet.format(cpl_range, fmt)
        
        #Format cho title cua data hang tuan
    worksheet.format("A12:H12", {
            "backgroundColor": {
                "red": 1.0,
                "green": 0.0,
                "blue": 0.0
            },
            "textFormat": {
                "foregroundColor": {
                    "red": 1.0,
                    "green": 1.0,
                    "blue": 1.0
                },
                "bold": True
            },
            "horizontalAlignment": "CENTER"
        })

    data_range = "A13:H100"
    worksheet.format(data_range, {
            "borders": {
                "top": {
                    "style": "SOLID",
                    "width": 1,
                    "color": {
                        "red": 0.0,
                        "green": 0.0,
                        "blue": 0.0
                    }
                },
                "bottom": {
                    "style": "SOLID",
                    "width": 1,
                    "color": {
                        "red": 0.0,
                        "green": 0.0,
                        "blue": 0.0
                    }
                },
                "left": {
                    "style": "SOLID",
                    "width": 1,
                    "color": {
                        "red": 0.0,
                        "green": 0.0,
                        "blue": 0.0
                    }
                },
                "right": {
                    "style": "SOLID",
                    "width": 1,
                    "color": {
                        "red": 0.0,
                        "green": 0.0,
                        "blue": 0.0
                    }
                }
            }
        })
        
        # Ket thuc Format cho data
    time.sleep(5)
        
         # Format title cho default table
    worksheet.format("C1:N1", {
            "backgroundColor": {
                "red": 1.0,
                "green": 0.0,
                "blue": 0.0
            },
            "textFormat": {
                "foregroundColor": {
                    "red": 1.0,
                    "green": 1.0,
                    "blue": 1.0
                },
                "bold": True
            },
            "horizontalAlignment": "CENTER"
        })
        

def formatting_report_table(worksheet,start_row,end_row):
    worksheet.format(f"C{start_row}:N{end_row}", {
            "backgroundColor": {
                "red": 1.0,
                "green": 1.0,
                "blue": 1.0
            }
        })

        # Thêm viền cho toàn bộ bảng dữ liệu
    worksheet.format(f"C2:N{end_row}", {
            "borders": {
                "top": {
                    "style": "SOLID",
                    "width": 1,
                    "color": {
                        "red": 0.0,
                        "green": 0.0,
                        "blue": 0.0
                    }
                },
                "bottom": {
                    "style": "SOLID",
                    "width": 1,
                    "color": {
                        "red": 0.0,
                        "green": 0.0,
                        "blue": 0.0
                    }
                },
                "left": {
                    "style": "SOLID",
                    "width": 1,
                    "color": {
                        "red": 0.0,
                        "green": 0.0,
                        "blue": 0.0
                    }
                },
                "right": {
                    "style": "SOLID",
                    "width": 1,
                    "color": {
                        "red": 0.0,
                        "green": 0.0,
                        "blue": 0.0
                    }
                }
            }
        })
        
        # Thêm viền cho hàng tổng 
    worksheet.format(f"C10:N10",
        {
            "borders": {
                "top": {
                    "style": "SOLID",
                    "width": 1,
                    "color": {
                        "red": 0.0,
                        "green": 0.0,
                        "blue": 0.0
                    }
                },
                "bottom": {
                    "style": "SOLID",
                    "width": 1,
                    "color": {
                        "red": 0.0,
                        "green": 0.0,
                        "blue": 0.0
                    }
                },
                "left": {
                    "style": "SOLID",
                    "width": 1,
                    "color": {
                        "red": 0.0,
                        "green": 0.0,
                        "blue": 0.0
                    }
                },
                "right": {
                    "style": "SOLID",
                    "width": 1,
                    "color": {
                        "red": 0.0,
                        "green": 0.0,
                        "blue": 0.0
                    }
                }
            }
        }
            
        )
        
    for column in ['C', 'I', 'K']:
        column_range = f"{column}{start_row}:{column}{end_row}"
        fmt = {
                "numberFormat": {
                    "type": "NUMBER",
                    "pattern": "#,##0"
                }
            }
        worksheet.format(column_range, fmt)


    