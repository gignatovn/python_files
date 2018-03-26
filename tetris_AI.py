import time

(y,m,d,h,min,start_sec,ms,mcs,dd) = time.localtime( time.time() )
(y,m,d,h,min,curr_sec,ms,mcs,dd) = time.localtime( time.time() )

while (curr_sec - start_sec) < 9.9:
    # 3 osnava kubcheta 2,4,7 ; 3,4,5 ; 2,2,4 ; 3,3,4 ; 2,3,4 ; 2,7 ; 3,5
    # 4 osnova kubcheta 4,4 ; 1,4,4; 3,6,6 ; 2,6,6

    (y,m,d,h,min,curr_sec,ms,mcs,dd) = time.localtime( time.time() )
