# IPv4_Calculator

IPv4_Calculator🧮 is developed for:
- Determine the 🌐[network class](https://docs.oracle.com/cd/E19504-01/802-5753/planning3-78185/index.html) (A, B, C); 
- Determine which category the address belongs to ([🔐private, 🔓public](https://www.geeksforgeeks.org/difference-between-private-and-public-ip-addresses/));
- Determine 📎[subnet attributes](https://www.simplilearn.com/tutorials/cyber-security-tutorial/what-is-sub-netting).

---
### Example 
```Python
python .\ipv4_calculator.py

Enter IP address of host: 24.156.99.202
Enter IP prefix: 12

IP address: 24.156.99.202/12

1. The network class - "A"
2. The address category - "Public Internet"
3. Subnetting attributes:

Number of octets:                    1st octet          2nd octet          3rd octet          4th octet
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Host Address (decimal):                 24                 156                99                 202
Mask (decimal):                         255                240                0                  0
Network Address (decimal):              24                 144                0                  0
First available host (decimal):         24                 144                0                  1
Last available host (decimal):          24                 159                255                254
Broadcast address (decimal):            24                 159                255                255
Host Address (binary):                00011000           10011100           01100011           11001010
Mask (binary):                        11111111           11110000           00000000           00000000
Network Address (binary):             00011000           10010000           00000000           00000000
First available host (binary):        00011000           10010000           00000000           00000001
Last available host (binary):         00011000           10011111           11111111           11111110
Broadcast address (binary):           00011000           10011111           11111111           11111111
Available number of addresses:                         32 - 12 = 20 , 2**20 - 2 = 1048574
```
