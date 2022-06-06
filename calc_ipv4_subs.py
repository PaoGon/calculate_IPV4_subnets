def calc_last_host(broad_addr:list)->list:

    last_host = broad_addr

    last_host[3] = last_host[3]-1
    
    return last_host


def calc_first_host(net_addr:list)->list:

    first_host = net_addr

    first_host[3] = first_host[3]+1
    
    return first_host
    


def calc_braodcast_addr(ip_add:list, prefix:int)-> list:
    '''param(list, int)
       
       calcuate the broadcast address

       returns the decimal format of broadcast address
    '''

    index = prefix//8
    broadcast_add = ip_add
    
    for octet in broadcast_add[index:]:
        host = octet[prefix%8:]
        for bit in host:
            if bit == '0':
                host = host[:host.index(bit)] + '1' + host[(host.index(bit))+1:]
        
        broadcast_add[index] = octet[:prefix%8] + host 


    dec_broad_add = [int(octet, 2) for octet in broadcast_add]
        
    return dec_broad_add
    


def calc_network_add(ip_add:list, prefix:int)-> list:
    '''
        ip_addb is binary form of the ip add
    '''

    index = prefix//8
    network_add = ip_add

    for octet in network_add[index:]:
        host = octet[prefix%8:]
        for bit in host:
            if bit == '1':
                host = host[:host.index(bit)] + '0' + host[(host.index(bit))+1:]
        
        network_add[index] = octet[:prefix%8] + host 


    dec_net_add = [int(octet, 2) for octet in network_add]


    return dec_net_add


    


def calc_host_per_sub(b_sub:int)->int:
    #b_sub == num_of_host_b_persub
    return (2**b_sub)-2


def num_of_host_b_persub(new_pref:int)->int:
    return 32 - new_pref
    

def calc_subnet_created(sub_bits:int):
    return 2**sub_bits

def calc_subnet_bits(n_prefix:int, o_prefix:int)-> int:
    return n_prefix - o_prefix


def get_prefix(arr:list)->int:
    prefix = 0
    for octets in arr:
        for bits in octets:
            if bits == '1':
                prefix += 1

    return prefix
            
    
 
def to_binary(arr:list)-> list:
    diff = 0
    new_arr = []
    # binary = ""
    for octet in arr:
        res ="{0:b}".format(int(octet))

        if len(res) < 8:
            diff = 8-len(res)
            new_arr.append(res + "0"*diff)
            # binary += (res + "0"*diff)
        else:
            new_arr.append(res)
            # binary += res


    # print(f"binary: {binary}")
    return new_arr


    

def main()-> None:

    ip_add = "192.168.200.139"
    new_sub_musk = "255.255.255.224"
    orig_sub_musk = "255.255.255.0"

    str_ip = ip_add.split(".")
    str_orig = orig_sub_musk.split(".")
    str_new = new_sub_musk.split(".")
    


    arr_ip_add = to_binary(str_ip)
    arr_orig = to_binary(str_orig)
    arr_new = to_binary(str_new)

    print(f"binary of IP addr: \t\t{arr_ip_add}")
    print(f"binary of new submusk: \t\t{arr_new}")
    print(f"binary of orgi submusk: \t{arr_orig}")

    orig_prefix = get_prefix(arr_orig)
    new_prefix = get_prefix(arr_new)

    subnet_bits = calc_subnet_bits(new_prefix, orig_prefix)
    created_subs = calc_subnet_created(subnet_bits)
    bits_per_subs = num_of_host_b_persub(new_prefix)
    host_per_subs = calc_host_per_sub(bits_per_subs)
    
    print("\n")
    print(f"orig prefix: {orig_prefix}")
    print(f"new prefix: {new_prefix}")

    print(f"no. of subnets bits: {subnet_bits}")
    print(f"no. of subnets created: {created_subs}")
    print(f"no. of subnets created: {bits_per_subs}")
    print(f"no. of subnets created: {host_per_subs}")
    print("\n")


    # calculate network address

    net_addr = calc_network_add(arr_ip_add, new_prefix)
    
    broad_addr = calc_braodcast_addr(arr_ip_add, new_prefix)
    print(f"network address: \t\t{net_addr}")
    print(f"broadcast_address: \t\t{broad_addr}")
    
    first_host = calc_first_host(net_addr)
    last_host = calc_last_host(broad_addr)
    
    print(f"Address of First host: \t\t{first_host}")
    print(f"Address of Last host: \t\t{last_host}")



if __name__ == "__main__":
    main()
