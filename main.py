from userProfile.userProfile import userProfile

def main():
    print ("main")
    userProfileIns = userProfile("Arun Prasath J")
    userProfileIns.login()
    userProfileIns.profileData()
    
if(__name__ == '__main__'):
    main()