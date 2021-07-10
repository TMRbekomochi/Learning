# coding: utf-8
import math

#表示設定
DISPLAY_ROW = 7     #縦幅
DISPLAY_COLUMN = 7  #横幅
DISPLAY_CHAR = '*'  #表示部文字設定
DISPLAY_SPACE = ' '  #空白部文字設定

#数字ごとのLED表示設定
#    a
#  b  c
#    d
#  e  f
#    g
#                  gfedcba
SEVENSEGMENT_0 = 0b1110111
SEVENSEGMENT_1 = 0b0100100
SEVENSEGMENT_2 = 0b1011101
SEVENSEGMENT_3 = 0b1101101
SEVENSEGMENT_4 = 0b0101110
SEVENSEGMENT_5 = 0b1101011
SEVENSEGMENT_6 = 0b1111010
SEVENSEGMENT_7 = 0b0100101
SEVENSEGMENT_8 = 0b1111111
SEVENSEGMENT_9 = 0b1101111
SEGMENTLED_NUM = 7
SEVENSEGMENT = [SEVENSEGMENT_0,
                SEVENSEGMENT_1,
                SEVENSEGMENT_2,
                SEVENSEGMENT_3,
                SEVENSEGMENT_4,
                SEVENSEGMENT_5,
                SEVENSEGMENT_6,
                SEVENSEGMENT_7,
                SEVENSEGMENT_8,
                SEVENSEGMENT_9]

#LED設定
DISPLAY_HIGHT = math.floor((DISPLAY_ROW - 3) / 2)
DISPLAY_MIDDLE = 0
DISPLAY_LEFT = 1
DISPLAY_RIGHT = 2
SEGMENT_LED_OFF       = 0b0
SEGMENT_LED_LEFTON    = 0b1
SEGMENT_LED_RIGHTON   = (0b1) << (DISPLAY_COLUMN - 1)
SEGMENT_LED_MIDDLE_ON = (SEGMENT_LED_LEFTON | SEGMENT_LED_RIGHTON) ^ ~(0b00)


N = int(input())
dispSegment = SEVENSEGMENT[N]

#LED点灯箇所の作成
disp = [SEGMENT_LED_OFF] * DISPLAY_ROW
for i in range(SEGMENTLED_NUM):
    segLED = i % 3
    p = int(math.floor(i/3) * (DISPLAY_HIGHT + 1))

    #a,d,g
    if segLED == DISPLAY_MIDDLE and (dispSegment >> i) & 0b01:
        disp[p] |= SEGMENT_LED_MIDDLE_ON
    #b,e
    elif segLED == DISPLAY_LEFT and (dispSegment >> i) & 0b01:
        p += 1
        for j in range(DISPLAY_HIGHT):
            disp[p + j] |= SEGMENT_LED_LEFTON
    #c, f
    elif segLED == DISPLAY_RIGHT and (dispSegment >> i) & 0b01:
        p += 1
        for j in range(DISPLAY_HIGHT):
            disp[p + j] |= SEGMENT_LED_RIGHTON

#LED表示
for d in disp:
    for i in range(DISPLAY_COLUMN):
        if (d >> i) & 0b01:
            print(DISPLAY_CHAR, end='')
        else:
            print(DISPLAY_SPACE, end='')
    print("")
