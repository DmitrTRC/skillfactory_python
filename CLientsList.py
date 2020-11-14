from db.guest_base import guest_lst

if __name__ == '__main__':
    for guest in guest_lst:
        if guest.is_invited:
            print(guest)
