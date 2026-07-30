## AND case  == both condition must be TRUE

age = 25

had_license = True

can_drive = age>=16 and had_license

print(can_drive)


## OR case == either one condition is true in or-case

had_license = False

can_drive = age>16 or had_license

print(can_drive)