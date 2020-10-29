from pathlib import Path

dB = Path('DataBase')

# User Profiles
userProfiledB = dB / 'userProfile'
userProfileFileName = userProfiledB / 'userProfile.xlsx'

userProfileSheet = 'userProfile'
strategyListSheet = 'strategyList'

# Trade Strategy
tradeStrategydB = dB / 'tradeStrategy'
stockListFileName = 'stockList.xlsx'