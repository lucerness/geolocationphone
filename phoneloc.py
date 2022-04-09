import argparse
import requests
import json
def found(phone=''):
        response = requests.get(f'https://mobile-tracker.biz/emulator/check?driver=geo&country=RU&provider=phone&uid=+{phone}&mode=undefined&_=1648381248958')
        decode_text = json.loads(response.text)
        location = decode_text.get('location')
        del location['geo_country']
        print('Results is ', '\n', location)
def main():
    parser = argparse.ArgumentParser(description="phone script")
    parser.add_argument("-n", dest="phone", required=True)
    args = parser.parse_args()
    compl =  found(args.phone)
    print(compl)
if __name__ == '__main__':
    main()
