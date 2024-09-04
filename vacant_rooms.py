def vacant_rooms(reserved_rooms,total_reserved,total_rooms):
    vacant=total_rooms-total_reserved
    return vacant

reserved_rooms=[1,2,3,4,5,6,7,8]
total_reserved=len(reserved_rooms)
total_rooms=10

result=vacant_rooms(reserved_rooms,total_reserved,total_rooms)
print(result)