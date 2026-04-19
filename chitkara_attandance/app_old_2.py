from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import chromedriver_autoinstaller
import pandas as pd
from datetime import datetime



# Please select dates here
today_date = [["05-May-25", "06-May-25", "07-May-25", "08-May-25"],
              ["05-May-25", "06-May-25", "07-May-25", "08-May-25"]]



# Install and set up ChromeDriver
chromedriver_autoinstaller.install()
options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Open the website
url = "https://cuiet.codebrigade.in/"
driver.get(url)


try:
    wait = WebDriverWait(driver, 20)

    # Locate username and password fields
    username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#txtUsername")))
    password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#txtPassword")))

    # Enter credentials Username and password
    username_field.send_keys("ET118")
    password_field.send_keys("ET118@")  
    print("✅ Credentials entered successfully.")

    # Locate and click the Sign In button
    sign_in_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='image']")))
    try:
        sign_in_button.click()
        print("✅ Sign In button clicked.")
    except:
        driver.execute_script("arguments[0].click();", sign_in_button)
        print("✅ Sign In button clicked using JavaScript.")

    # Wait for OTP page to load
    wait.until(EC.url_changes(url))
    print("🔑 OTP page loaded.")

    # Wait for user to manually enter OTP and submit
    input("Enter OTP, then press Enter here to continue...")

    # Search for 'Mark Daily Attendance' in menu
    
    for i in range(len(today_date)):
        df_c=[pd.read_csv("G-30-08-05.csv"),pd.read_csv("G-34-08-05.csv")]  #add df here

        df=df_c[i]

        df.columns = df.columns.str.strip()

        df = df[pd.to_numeric(df["Roll Number"], errors='coerce').notna()]  # Remove non-numeric values
        df["Roll Number"] = df["Roll Number"].astype(int)
        numbers = df["Roll Number"].tolist()

        for j in range(len(today_date[i])):
            present_students=0
            absent_students=0
            menu_lookup = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#menuLookup")))  
            menu_lookup.send_keys("Mark Daily Attendance")
            print("✅ Entered 'Mark Daily Attendance' in menu search.")

            # Wait for the dropdown to appear and click the option
            attendance_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Mark Daily Attendance')]")))
            attendance_option.click()
            print("✅ Selected 'Mark Daily Attendance' from dropdown.")

            # Data Selection
            buttons = driver.find_elements(By.CSS_SELECTOR, "button.multiselect.dropdown-toggle") 
            
            buttons[0].click()
            print("⏩Clicked on Time Table button")
            # Select 'JAN-JUNE2025' from the list
            option = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(., 'JAN-JUNE2025')]/input")))
            option.click()
            print("✅ Selected 'JAN-JUNE2025' from the dropdown.")

            
            buttons[1].click()
            print("⏩Clicked on Period Slot button")

            option_cs = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(., 'CSE - EVE - 50Mins')]/input")))
            option_cs.click()


            date_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#txtFromDate")))
            driver.execute_script("arguments[0].removeAttribute('readonly')", date_input)  # Remove readonly if needed
            date_input.clear()
            date_obj = datetime.strptime(today_date[i][j], "%d-%b-%y")

            # Convert back to desired format
            formatted_date = date_obj.strftime("%d-%m-%y")
            date_input.send_keys(formatted_date)
            print("✅ Date entered.")


            buttons[3].click()
            print("⏩Clicked on Class button")
            # Select 'JAN-JUNE2025' from the list
            option = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(., '2024-BE-CSE-AI-2 SEM')]/input")))
            option.click()
            print("✅ Selected Class")
            
            buttons[5].click()
            print("⏩Clicked on Subject button")
            option = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(., '24CAI0105 (Web Development Framework Using Python) - Theory')]/input")))
            option.click()
            print("✅ Selected Subject 2024-BE-CSE-AI-2 SEM")

            # Data Selection End

            input("Date is selected now, Select Periods and Groups,then press Enter ⏩ here to continue...")
            students = driver.find_elements(By.CSS_SELECTOR, "table#masterGridTable tbody tr")



            try:
                for student in students:
                    roll_no_element = student.find_element(By.CSS_SELECTOR, "td:nth-child(3)")  # Adjust the index if needed
                    select_element = student.find_element(By.CSS_SELECTOR, "select")

                    roll_no = roll_no_element.text.strip()
                    print(f"Extracted Roll No: '{roll_no}' (Type: {type(roll_no)})")

                    # Validate if roll_no is a proper number before conversion
                    if roll_no.isdigit():  # Only convert if it contains digits
                        num = int(roll_no)

                        print("num",num)
                        if num in numbers:
                            # status = df.loc[df["Roll Number"] == num, "Attendance"].values[0]
                            # status = df.loc[df["Roll Number"].astype(str) == num, today_date]
                            
                            status_series = df.loc[df["Roll Number"] == num, today_date[i][j]]
                            
                            status = status_series.values[0].strip().upper()
                            print(status)
                            if status.lower() == "p":
                                select_element.send_keys("Present")
                                present_students+=1
                            else:
                                select_element.send_keys("Absent")
                                absent_students+=1
                            print(f"✅ Marked {num} as {status}.")
                        else:
                            print(f"⚠️ Roll number {num} not found in the CSV.")
            
                    else:
                        print(f"⚠️ Skipping invalid roll number: '{roll_no}'")
            except Exception as e:
                print("❌ Some error:", e)

            print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
            print(f"🎉 Present students on {formatted_date} 🟢 = {present_students} 🎉")
            print(f"🎉 Absent students on {formatted_date} 🔴 = {absent_students}  🎉")
            print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
            input(f"Data is filled for {formatted_date}, press Enter for filling next date... ")

    print("😃 Happy To Help")

except Exception as e:
    print(f"❌ Error: {e}")


# Quit browser
driver.quit()
