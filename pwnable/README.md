# Pwnable Challenges

* [ ] 2017 Meepwn anotherarena
  - not working yet
* [ ] 2017 HUST RR2L
  - solved but not working yet
* [ ] 2017 HUST wind
  - solved but not working yet
* [x] 2017 0ctf babyheap
  - https://github.com/ktb88/ctf/tree/master/pwnable/0004_2017_0ctf_babyheap
  - x86-64 | FULL RELRO | NX | PIE
  - heap (overlay fast bin and small bin)
* [ ] 2017 0ctf EasiestPrintf
  - TODO: there is execution problem
  - i386 application running on debian
  - FSB
  - printf malloc, free condition (width)
* [x] 2017 BostonKeyParty memo
  - https://github.com/ktb88/ctf/tree/master/pwnable/0006_2017_bkp_memo
  - x86-64 | FULL RELO | NX
  - heap (fast bin)
  - logic bug to leak the libc address
* [x] 2016 openCTF tyro_heap
  - https://github.com/ktb88/ctf/tree/master/pwnable/0007_2016_openCTF_tyroheap
  - i386 | NX
  - heap buffer overflow
  - overwrite function pointer
* [x] 2017 0ctf diethard
  - https://github.com/ktb88/ctf/tree/master/pwnable/0008_2017_0ctf_diethard
  - x86-64 | NX
  - custom heap (?)
* [x] 2016 bctf bcloud
  - https://github.com/ktb88/ctf/tree/master/pwnable/0009_2017_bctf_bcloud
  - i386 | NX
  - heap (House of force)
  - leak by got overwritten
* [x] 2017 RCTF aiRcraft
  - https://github.com/ktb88/ctf/tree/master/pwnable/0010_2017_RCTF_aiRcraft
  - amd64 | NX | PIE | Partial Relro
  - Heap Exploit
  - double-free
  - use-after-free
  - overwritten function ptr
* [x] 2017 h3x0r mic for pwn
  - https://github.com/ktb88/ctf/tree/master/pwnable/0011_2017_h3x0r_MicForPwn
  - i386 | NX | SSP
  - Format String Bug (FSB)
  - Leak memory by SSP
* [x] 2017 bugsbunny Pwn50
  - https://github.com/ktb88/ctf/tree/master/pwnable/0012_2017_bugsbunny_pwn50
  - Simple Pwnable Challenge
* [x] 2017 bugsbunny Pwn100
  - https://github.com/ktb88/ctf/tree/master/pwnable/0012_2017_bugsbunny_pwn100
  - i386
  - return to shellcode
* [x] 2017 bugsbunny Pwn150
  - https://github.com/ktb88/ctf/tree/master/pwnable/0012_2017_bugsbunny_pwn150
  - x86_64 simple stack bof
  - gdb : set follow-fork-mode [child | parent] 
* [x] 2017 bugsbunny Pwn200
  - https://github.com/ktb88/ctf/tree/master/pwnable/0012_2017_bugsbunny_pwn200
  - overwrite got
* [x] 2017 bugsbunny Pwn250
  - https://github.com/ktb88/ctf/tree/master/pwnable/0012_2017_bugsbunny_pwn250
  - 64bit One-shot gadget
  - rdi, rsi, edx
* [ ] 2017 bugsbunny Pwn300
  - tired to make the shellcode.... :(
  - 64bit shellcode
  - Alphanumeric shellcode

