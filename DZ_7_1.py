from pprint import pprint
'''
1. Создайте в директории проекта текстовый файл с раширением txt
2. Добавьте в этот файл следующий текст
# -*- coding: utf-8 -*-
My soul is dark - Oh! quickly string
The harp I yet can brook to hear;
And let thy gentle fingers fling
Its melting murmurs o'er mine ear.
If in this heart a hope be dear,
That sound shall charm it forth again:
If in these eyes there lurk a tear,
'Twill flow, and cease to burn my brain.

But bid the strain be wild and deep,
Nor let thy notes of joy be first:
I tell thee, minstrel, I must weep,
Or else this heavy heart will burst;
For it hath been by sorrow nursed,
And ached in sleepless silence, long;
And now 'tis doomed to know the worst,
And break at once - or yield to song.

3. Создайте переменную с этим файлом
4. Распечатайте содержимое текстового файла в консоль
5. Закройте файл
'''

poem = 'DZ_7_1_.txt'
file = open(poem, mode='rb')
poem_content = file.read()
pprint(poem_content)
file.close()