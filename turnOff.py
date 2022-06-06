from subprocess import call
from plyer import notification
from time import sleep
from datetime import datetime

def main():

  def turnOffPc():
    hoursDivider = [2, 3, 6]
    seconds : int = 3600
    i = 0
    while True:
      while i < len(hoursDivider):
        data = datetime.now()
        notification.notify(title="Computador vai desligar em {} {}.".format(int(seconds / 60), formatStr(seconds)),
                            message="{} - Aproveite e faça o backup do servidor local para o google drive.".format(data.strftime("%H:%M")),
                            toast=False
                            )
        seconds /= hoursDivider[i]
        sleep(seconds)
        i += 1
      else:
        call(['shutdown', '/s', '/f'])
        break

  def formatStr(sec):
    if sec <= 600:
      return 'minuto'
    else:
      return 'minutos'
  
  turnOffPc()

if __name__ == '__main__':
  main()
