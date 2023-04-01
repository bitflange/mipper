import mip
import requirements
import uos

def print_free():
    fs_stat = uos.statvfs('/')
    fs_size = fs_stat[0] * fs_stat[2]
    fs_free = fs_stat[0] * fs_stat[3]
    print(f"= file system: {fs_free:,} free of {fs_size:,} bytes ({fs_free/fs_size*100}%)")

def install():
    for pkg in requirements.src_list:
        short_name, mip_path = pkg
        try:
            print(f"importing {short_name}", sep="")
            __import__(short_name)
        except:
            try:
                print("... not found, attempting to install with mip")
                mip.install(mip_path)
                __import__(short_name)
                fsize = uos.stat(f'/lib/{short_name}.py')[6]
                print(f'+ {short_name}, {fsize} bytes')
            except:
                print(f"FATAL:  Cannot retrieve {short_name} with mip (target: {mip_path})!")
    print_free()
