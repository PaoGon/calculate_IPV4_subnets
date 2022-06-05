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
    for octet in arr:
        res ="{0:b}".format(int(octet))

        print(f"len:{len(res)}")
        if len(res) < 8:
            diff = 8-len(res)
            new_arr.append(res + "0"*diff)
        else:
            new_arr.append(res)

    return new_arr


    

def main()-> None:
    # arr_new = []
    orig_sub_musk = input("Enter original subnet musk: ")
    new_sub_musk = input("Enter new new subnet musk: ")

    str_orig = orig_sub_musk.split(".")
    str_new = new_sub_musk.split(".")


    arr_orig = to_binary(str_orig)
    arr_new = to_binary(str_new)

    print(arr_orig)
    print(arr_new)

    orig_prefix = get_prefix(arr_orig)
    new_prefix = get_prefix(arr_new)
    
    print(f"orig prefix: {orig_prefix}")
    print(f"new prefix: {new_prefix}")

if __name__ == "__main__":
    main()
