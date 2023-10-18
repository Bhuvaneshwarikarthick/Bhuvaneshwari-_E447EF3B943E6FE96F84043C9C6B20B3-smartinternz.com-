def  Leapyear( year):
    if ( year % 400 == 0) and (year % 100 !=0):
         return True
    else:
          return False
year=2013
if Leapyear(year):
    print('{} is a leap year.'.format( year))
else:
    print('{} is not a leap year.'.format( year))
