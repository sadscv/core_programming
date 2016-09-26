#! /usr/bin/env python

'''process the carddata file.input as a string and use a log file to trace the procession'''

def safe_float(obj):
    'safe version of float()'
    try:
        retval = float(obj)
    except (ValueError,TypeError) as e:
        retval = str(e)
    return retval

def main():
    'handle all the data processing'
    with open('cardlog.txt', 'w') as log:
    # log = open('cardlog.txt','w')
        try:
            ccfile = open('carddata.txt', 'r')
        except IOError as e:
            log.write('no txns this month\n')
            return

    total = 0.00
    with open('cardlog.txt', 'w') as log:
        log.write('account log:\n')
        for line in ccfile:
            result = safe_float(line)
            if isinstance(result, float):
                total += result
                log.write('data...processed\n')
            else:
                log.write('ignored:%s' % result)
    print('$%.2f (new balance)' % (total))


if __name__ == '__main__':
    main()