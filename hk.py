import ipaddress

# 文件路径
input_file = 'hk.csv'
output_file = 'hk.txt'

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        parts = line.strip().split('\t')
        if len(parts) < 2:
            continue
        start_ip_str, end_ip_str = parts[0], parts[1]
        try:
            start_ip = ipaddress.IPv4Address(start_ip_str)
            end_ip = ipaddress.IPv4Address(end_ip_str)
            current_ip = start_ip
            while current_ip <= end_ip:
                outfile.write(str(current_ip) + '\n')
                current_ip += 1
        except ValueError:
            continue

print(f"所有 IP 已写入到 {output_file}")
