importos, time
#Take the birthday lookup file from home directory
file_path = os.getenv('HOME') + '/birth_day_lookup.txt'
defcheck_birthday():
   lookup_file = open(file_path, 'r') #open the lookup file as read mode
   today = time.strftime('%d-%B') #get the todays date as dd-Month format
   bday_flag = 0
   #loop through each entry in the birthday file, and check whether the day is present or not
   for entry inlookup_file:
      if today in entry:
         line = entry.split(' ') #cut the line on spaces to get name and surname
         bday_flag = 1
         os.system('notify-send "Today is '+line[1]+' '+line[2]+'\'s Birthday"')
   ifbday_flag == 0:
      os.system('notify-send "No birthday for today is listed"')
check_birthday()
