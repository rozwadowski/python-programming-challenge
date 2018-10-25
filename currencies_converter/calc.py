import urllib
import json


def calc(amount, i, j, val, code):
    print amount, code[i], " = ", round(amount*val[i]/val[j], 2), code[j]


def main():
    code = ["PLN"]
    val = [1.0]
    urls = ["http://api.nbp.pl/api/exchangerates/tables/a/today/?format=json",
            "http://api.nbp.pl/api/exchangerates/tables/b/?format=json"]
    for u in urls:
        url = urllib.urlopen(u)
        data = json.loads(url.read())[0]
        print "Dane z", data["effectiveDate"]
        print "Dostepne obce waluty: ",
        for curr in data["rates"]:
            print curr["code"],
            code.append(str(curr["code"]))
            val.append(float(curr["mid"]))
        print
    try:
        print "Podaj zapytanie w postaci x.xxx PLN EUR"
        while True:
            command = raw_input(": ")
            command = command.split()
            if len(command) != 3:
                print "Nieprawidlowe zapytanie"
            else:
                if not command[1].upper() in code
                or not command[2].upper() in code:
                    print "Blad wyboru walut"
                else:
                    calc(float(command[0]), code.index(command[1].upper()),
                         code.index(command[2].upper()), val, code)
    except KeyboardInterrupt:
        print "\nDo widzenia "


if __name__ == "__main__":
    main()
