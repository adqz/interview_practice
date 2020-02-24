import re
class Solution:
    def validIPAddress(self, IP: str) -> str:
        if self.is_IPV4:
            is_valid_IPV4 = self.is_IPV4_address_valid(IP)
        if self.is_IPV6:
            is_valid_IPV6 = self.is_IPV6_address_valid(IP)
        
        if is_valid_IPV4:
            return 'IPv4'
        elif is_valid_IPV6:
            return 'IPv6'
        else:
            return 'Neither'
    
    def is_IPV4(self, IP):
        if '.' in set(IP):
            return True
        return False

    def is_IPV6(self, IP):
        if ':' in set(IP):
            return True
        return False

    def is_IPV4_address_valid(self, IP):
        address_numbers = IP.split('.')
        if len(address_numbers) != 4:
            return False
        for number in address_numbers:
            if len(number) > 4 or len(number) < 1:
                return False
            if number[0] == '0' and len(number) > 1:
                return False
            if not(number.isdigit()):
                return False
            try:
                number = int(number)
            except ValueError:
                return False
            if not( 0 <= number <= 255 ):
                return False
        return True
    def is_IPV6_address_valid(self, IP):
        address_numbers = IP.split(':')
        if len(address_numbers) != 8:
            return False
        for number in address_numbers:
            if len(number) > 4:
                return False
            is_valid_hexadecimal = bool(re.search(r'^[a-fA-F0-9]', number))
            print(number, is_valid_hexadecimal)
            if not(is_valid_hexadecimal):
                return False
            # # Checking if valid hexadecimal
            # try:
            #     int(number, 16)
            # except ValueError:
            #     return False
        return True
            

if __name__ == "__main__":
    sol = Solution()
    # print(sol.validIPAddress("172.16.254.1")) #IPv4
    # print(sol.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334")) #IPv6
    # print(sol.validIPAddress("256.256.256.256")) #Neither
    # print(sol.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
    print(sol.validIPAddress("20EE:FGb8:85a3:0:0:8A2E:0370:7334"))