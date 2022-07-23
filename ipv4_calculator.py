# function for convert decimal to binary
def dec_to_bin(num):
    bin_str = ''
    while num != 0:
        bin_str += '1' if num % 2 == 1 else '0'
        num = num // 2
    while len(bin_str) != 8:
        bin_str += '0'
    return bin_str[::-1]


# function to determine the correctness of IP address
def correct_ip(address):
    L = address.split('.')
    count = 0
    for i in L:
        if 0 <= int(i) <= 255:
            count += 1
        else:
            return False
    if count == 4:
        return True




# Output data
# Entering IP address
host_address = input('Enter IP address of host: ')


while True:
    if correct_ip(host_address) == True:
        break
    else:
        host_address = input('Please, Enter correct IP address of host: ')

          
ip_prefix = input('Enter IP prefix: ')

print(f'IP address: {host_address}/{ip_prefix}\n')



# 1. Determine the network class(A, B, C)

n1 = 1  # n1 - first step

ip_list = host_address.split('.')  # translate each octet of the IP address into a list element

if 0 <= int(ip_list[0]) < 128:
    print(f'{n1}. The network class - "A"')

elif 128 <= int(ip_list[0]) < 192:
    print(f'{n1}. The network class - "B"')

elif 192 <= int(ip_list[0]) < 223:
    print(f'{n1}. The network class - "C"')



# 2. Determine which category the address belongs to (private, public)

n2 = 2  # n2 - second step

octet_list = [str(i+1) + 'st octet' for i in range(len(ip_list))]  # create a list with the serial numbers of the octets
ip_dict = {}
for key, value in zip(octet_list, ip_list):  # create a dictionary with IP address elements divided into octets
    ip_dict[key] = int(value)


if ip_dict['1st octet'] == 10:
    print(f'{n2}. The address category - "Private Internet"\n')
    
elif ip_dict['1st octet'] == 172 and 16 <= ip_dict['2st octet'] <= 31:
    print(f'{n2}. The address category - "Private Internet"\n')
    
elif ip_dict['1st octet'] == 192 and ip_dict['2st octet'] == 168:
    print(f'{n2}. The address category - "Private Internet"\n')
    
else:
    print(f'{n2}. The address category - "Public Internet"\n')



# 3. Determine subnet attributes

n3 = 3  # n3 - third step

mask_bin = int(ip_prefix)*'1' + (32-int(ip_prefix))*'0'

mask_bin_list = []
for i in range(0, len(mask_bin), 8):
    mask_bin_list.append(mask_bin[i:i+8])


mask_decimal_list = [int(('0b'+i), 2) for i in mask_bin_list]

ip_bin_list = [dec_to_bin(int(i)) for i in ip_list]


subnet_decimal_list = []
for i in range(4):
    subnet_decimal_list.append(int(('0b'+ mask_bin_list[i]),2) & int(('0b'+ ip_bin_list[i]),2))


subnet_bin_list = [dec_to_bin(i) for i in subnet_decimal_list]


first_host_address = subnet_decimal_list[:3] + [subnet_decimal_list[3] + 1]


last_host_address = []
if 9 <= int(ip_prefix) <= 16:
    last_host_address = subnet_decimal_list[:1] + [subnet_decimal_list[1] + 2**(16-int(ip_prefix)) - 1] + [255, 254]
elif 17 <= int(ip_prefix) <= 24:
    last_host_address = subnet_decimal_list[:2] + [subnet_decimal_list[2] + 2**(24-int(ip_prefix)) - 1] + [254]
elif 25 <= int(ip_prefix) <= 30:
    last_host_address = subnet_decimal_list[:3] + [subnet_decimal_list[3] + 2**(32-int(ip_prefix)) - 2]
elif 1 <= int(ip_prefix) <= 8:
    last_host_address = [subnet_decimal_list[0] + 2**(8-int(ip_prefix)) - 1] + [255, 255, 254]


broadcast_address = []
if 9 <= int(ip_prefix) <= 16:
    broadcast_address = subnet_decimal_list[:1] + [subnet_decimal_list[1] + 2**(16-int(ip_prefix)) - 1] + [255, 255]
elif 17 <= int(ip_prefix) <= 24:
    broadcast_address = subnet_decimal_list[:2] + [subnet_decimal_list[2] + 2**(24-int(ip_prefix)) - 1] + [255]
elif 25 <= int(ip_prefix) <= 30:
    broadcast_address = subnet_decimal_list[:3] + [subnet_decimal_list[3] + 2**(32-int(ip_prefix)) - 1]
elif 1 <= int(ip_prefix) <= 8:
    broadcast_address = [subnet_decimal_list[0] + 2**(8-int(ip_prefix)) - 1] + [255, 255, 255]     
        

print('Number of octets:' + 20*' ', end='')
for i in ip_dict:
    if i == '4st octet':
        print(i, end='\n')
    else:
        print(i, end=10*' ')

print('Host Address (decimal):' + 17*' ', end='')
for i in ip_dict:
    if i == '4st octet':
        print(ip_dict[i], end='\n')
    else:
        if len(str(ip_dict[i])) == 3:
            print(ip_dict[i], end=16*' ')
        elif len(str(ip_dict[i])) == 2:
            print(ip_dict[i], end=17*' ')
        else:
            print(ip_dict[i], end=17*' ')

print('Mask (decimal): ' + 24*' ', end='')
for i in mask_decimal_list:
    if len(str(i)) == 3:
        print(i, end=16*' ')
    elif len(str(i)) == 2:
        print(i, end=17*' ')
    else:
        print(i, end=18*' ')
    

print()

print('Network Address (decimal): ' + 13*' ', end='')
for i in subnet_decimal_list:
    if len(str(i)) == 3:
        print(i, end=16*' ')
    elif len(str(i)) == 2:
        print(i, end=17*' ')
    else:
        print(i, end=18*' ')

print()

print('First available host(decimal): ' + 9*' ', end='')
for i in first_host_address:
    if len(str(i)) == 3:
        print(i, end=16*' ')
    elif len(str(i)) == 2:
        print(i, end=17*' ')
    else:
        print(i, end=18*' ')

print()

print('Last available host(decimal): ' + 10*' ', end='')
for i in last_host_address:
    if len(str(i)) == 3:
        print(i, end=16*' ')
    elif len(str(i)) == 2:
        print(i, end=17*' ')
    else:
        print(i, end=18*' ')

print()

print('Broadcast address (decimal): ' + 11*' ', end='')
for i in broadcast_address:
    if len(str(i)) == 3:
        print(i, end=16*' ')
    elif len(str(i)) == 2:
        print(i, end=17*' ')
    else:
        print(i, end=18*' ')

print()

print('Host Address (binary):' + 16*' ', end='')
for i in ip_bin_list:
    print(i, end=11*' ')

print()

print('Mask (binary): ' + 23*' ', end='')
for i in mask_bin_list:
    print(i, end=11*' ')

print()

print('Network Address(binary): ' + 12*' ', end='')
for i in subnet_bin_list:
    print(i, end=11*' ')

print()

print('First available host(binary): ' + 7*' ', end='')
for i in first_host_address:
    print(dec_to_bin(i), end=11*' ')

print()

print('Last available host(binary): ' + 9*' ', end='')
for i in last_host_address:
    print(dec_to_bin(i), end=11*' ')

print()

print('Broadcast address (binary): ' + 10*' ', end='')
for i in broadcast_address:
    print(dec_to_bin(i), end=11*' ')

print()

print('Available number of addresses: ' + 24*' ', end='')
n = 32-int(ip_prefix)
print(f'32 - {ip_prefix} =', 32-int(ip_prefix), f', 2**{n} - 2 =', (2**(32-int(ip_prefix)) - 2), end='\n')
