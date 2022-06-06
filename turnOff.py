from subprocess import call
from plyer import notification
from time import sleep
from datetime import datetime

def main():
  def turnOffPc():
    hoursDivider = [2, 3, 6]
    hoursStr = ['s', 's', '']
    seconds : int = 3600
    i = 1
    while True:
      while i <= len(hoursDivider):
        data = datetime.now()
        notification.notify(title="Computador vai desligar em {} minuto{}.".format(int(seconds / 60), hoursStr[i-1]),
                            message="{} - Aproveite e faça o backup do servidor local para o google drive.".format(data.strftime("%H:%M")),
                            toast=False
                            )
        seconds /= hoursDivider[i-1]
        sleep(seconds)
        i += 1
      else:
        turnOffCommand()
        break

  def turnOffCommand():
    call(['shutdown', '/s', '/f'])
  
  turnOffPc()


if __name__ == '__main__':
  main()
