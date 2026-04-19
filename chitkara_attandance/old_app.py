# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# import chromedriver_autoinstaller
# import pandas as pd
# from datetime import datetime
# # Load CSV file
# # df = pd.read_csv("g-29-1.csv")  # Replace with the actual filename
# df = pd.read_csv("G-34-22-03.csv")  # Replace with the actual filename

# # Remove spaces from column names
# df.columns = df.columns.str.strip()

# # Remove NaN values
# df = df[pd.to_numeric(df["Roll Number"], errors='coerce').notna()]  # Remove non-numeric values
# df["Roll Number"] = df["Roll Number"].astype(int)
# numbers = df["Roll Number"].tolist()


# today_date = ["17-Mar-25","18-Mar-25","19-Mar-25", "20-Mar-25", "22-Mar-25"]



# # Install and set up ChromeDriver
# chromedriver_autoinstaller.install()
# options = webdriver.ChromeOptions()
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)

# # Open the website
# url = "https://cuiet.codebrigade.in/"
# driver.get(url)




# try:
#     wait = WebDriverWait(driver, 20)

#     # Locate username and password fields
#     username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#txtUsername")))
#     password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#txtPassword")))

#     # Enter credentials
#     username_field.send_keys("ET118")
#     password_field.send_keys("ET118@")
#     print("✅ Credentials entered successfully.")

#     # Locate and click the Sign In button
#     sign_in_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='image']")))
#     try:
#         sign_in_button.click()
#         print("✅ Sign In button clicked.")
#     except:
#         driver.execute_script("arguments[0].click();", sign_in_button)
#         print("✅ Sign In button clicked using JavaScript.")

#     # Wait for OTP page to load
#     wait.until(EC.url_changes(url))
#     print("🔑 OTP page loaded.")

#     # Wait for user to manually enter OTP and submit
#     input("Enter OTP manually in the browser and submit it, then press Enter here to continue...")

#     # Search for 'Mark Daily Attendance' in menu
    
#     for i in range(len(today_date)):
#         menu_lookup = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#menuLookup")))  
#         menu_lookup.send_keys("Mark Daily Attendance")
#         print("✅ Entered 'Mark Daily Attendance' in menu search.")

#         # Wait for the dropdown to appear and click the option
#         attendance_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Mark Daily Attendance')]")))
#         attendance_option.click()
#         print("✅ Selected 'Mark Daily Attendance' from dropdown.")

#         # Click the multiselect dropdown button
#         dropdown_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.multiselect.dropdown-toggle")))
#         dropdown_button.click()
#         print("✅ Opened the Time Table dropdown.")

#         # Select 'JAN-JUNE2025' from the list
#         option = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(., 'JAN-JUNE2025')]/input")))
#         option.click()
#         print("✅ Selected 'JAN-JUNE2025' from the dropdown.")

#         # 
#         # Enter Date
#         date_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#txtFromDate")))
#         driver.execute_script("arguments[0].removeAttribute('readonly')", date_input)  # Remove readonly if needed
#         date_input.clear()
#         date_obj = datetime.strptime(today_date[i], "%d-%b-%y")

#         # Convert back to desired format
#         formatted_date = date_obj.strftime("%d-%m-%y")
#         date_input.send_keys(formatted_date)
#         print("✅ Date entered.")

#         input("Date is selected now, Enter other details, then press Enter here to continue...")
#         students = driver.find_elements(By.CSS_SELECTOR, "table#masterGridTable tbody tr")

#         try:
#             for student in students:
#                 roll_no_element = student.find_element(By.CSS_SELECTOR, "td:nth-child(3)")  # Adjust the index if needed
#                 select_element = student.find_element(By.CSS_SELECTOR, "select")

#                 roll_no = roll_no_element.text.strip()
#                 print(f"Extracted Roll No: '{roll_no}' (Type: {type(roll_no)})")

#                 # Validate if roll_no is a proper number before conversion
#                 if roll_no.isdigit():  # Only convert if it contains digits
#                     num = int(roll_no)

#                     print("num",num)
#                     if num in numbers:
#                         # status = df.loc[df["Roll Number"] == num, "Attendance"].values[0]
#                         # status = df.loc[df["Roll Number"].astype(str) == num, today_date]
#                         status_series = df.loc[df["Roll Number"] == num, today_date[i]]
#                         status = status_series.values[0].strip().upper()
#                         print(status)
#                         if status.lower() == "p":
#                             select_element.send_keys("Present")
#                         else:
#                             select_element.send_keys("Absent")
#                         print(f"✅ Marked {num} as {status}.")
#                     else:
#                         print(f"⚠️ Roll number {num} not found in the CSV.")
        
#                 else:
#                     print(f"⚠️ Skipping invalid roll number: '{roll_no}'")
#         except Exception as e:
#             print("❌ Some error:", e)

#         input(f"Data is filled for {formatted_date}, Cross check once and click on submit manually, press Enter for filling next date... ")

        
    



#     print("🚀 Ready for next automation steps!")

# except Exception as e:
#     print(f"❌ Error: {e}")


# # Quit browser
# driver.quit()
