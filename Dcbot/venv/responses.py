from random import choice ,randint
import datetime

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    inputs: str = user_input.lower()
    tday = datetime.date.today()

    

    if lowered == "lesson":
       return 'which'
    elif lowered == '0':
       return 'ორშაბათი 21:00 - 23:00 and ხუთშაბათი 21:00 - 23:00'
    elif lowered == '4':
       return 'სამშაბათი 21:00 - 23:00 and პარასკევი 21:00 - 23:00'
    elif lowered == '5':
       return 'ოთხშაბათი 21:00 - 23:00 and შაბათი 21:00 - 23:00'
    elif lowered == '6':
       return 'სამშაბათი 19:30 - 21:00 and პარასკევი 19:00 - 21:00'
    elif lowered == '7':
       return 'ოთხშაბათი 19:00 - 21:00 and შაბათი 19:00 - 21:00'
    elif lowered == '9':
       return 'ოთხშაბათი 21:00 - 23:00 and შაბათი 21:00 - 23:00'
    elif lowered == '11':
       return 'სამშაბათი 19:00 - 21:00 and შაბათი 17:00 - 19:00 and კვირა 19:00 - 21:00'
    elif lowered == '12':
       return 'შაბათი 13:00 - 15:00 and კვირა 11:00 - 13:00'
    elif lowered == '13':
       return 'ორშაბათი 21:00 - 23:00 and ხუთშაბათი 21:00 - 23:00'
    elif lowered == '14':
       return 'ორშაბათი 19:00 - 21:00 and პარასკევი 19:00 - 21:00'
    elif lowered == '15':
       return 'ხუთშაბათი 19:00 - 21:00 and კვირა 21:00 - 23:00'
    elif lowered == '16':
       return 'სამშაბათი 21:00 - 23:00 and პარასკევი 21:00 - 23:00'
    elif lowered == '17':
       return 'კვირა 13:00 - 15:00'
    elif lowered == '18':
       return 'შაბათი 15:00 - 17:00'
    elif lowered == '19':
       return 'კვირა 15:00 - 17:00'
    elif lowered == '20':
       return 'კვირა 17:00 - 19:00'
    elif lowered == 'today':
       if tday.weekday() == 3:
          return 'ხუთშაბათი'
       elif tday.weekday() == 0:
          return 'ორშაბათი'
       elif tday.weekday() == 1:
          return 'სამშაბათი'
       elif tday.weekday() == 2:
          return 'ოთხშაბათი'
       elif tday.weekday() == 4:
          return 'პარასკევი'
       elif tday.weekday() == 5:
          return 'შაბათი'
       elif tday.weekday() == 6:
          return 'კვირა'
    elif lowered == 'ორშაბათი':
       return '012,13,14'
    elif lowered == 'სამშაბათი':
       return '4,11,16'
    elif lowered == 'ოთხშაბათი':
       return '5,7,9'
    elif lowered == 'ხუთშაბათი':
       return '012,13,15'
    elif lowered == 'პარასკევი':
       return '4,6,14,16'
    elif lowered == 'შაბათი':
       return '5,7,9,11,12,18'
    elif lowered == 'კვირა':
       return '11,12,15,17,19,20'
    else:
       return 'please type everything on georgian,commands:lesson,today,ორშაბათი-დან,კვირა-მდე,All groups from Group 0 to Group 20'

    
    
    
    
