
# Level-4
## 6-round DES
### Commands used in the game to reach the first ciphertext
go-> dive-> dive-> take (dead)-> connection re-establish 

go-> dive-> dive-> up-> take-> back-> go-> wave-> back-> enter-> pluck-> back-> back-> thrnxxtzy-> read-> the_magic_of_wand-> read-> password


### Cryptosystem was used at this level
6-round DES





### Observations used to figure out the cryptosystem
 
In this we have to figure out a password which was encrypted using either 4, 6 or 10 round DES. From the spirit's hint, we understood that the cryptosystem for this level is either 4 round DES or 6 round DES. The chances of it being 10 round DES were significantly less. So we started with assuming 6 round DES.

After entering "password" , we get our ciphertext which is

"hhjqgnpisfltfrpjlffpmfhlrfukmrsq"

 It was given that two letters were for one byte and DES has a block size of 64 bits or 8 bytes so 16 letters represented 1 block size. Because there were only 16 letters in the output which we found after doing frequency analysis which were from ‘f’ to ‘u’. so while generating plaintext for the attack, we used letters only from [f,u]. The block size of DES is 8 bytes, so each block contains 16 letters. each alphabet was mapped with a number from 0 to 15. 


Chosen plain text attack is used to break DES encryption. In this, we used differential cryptanalysis to generate plain text pairs, pass them to the system to get corresponding ciphertext pairs, and then used these to find the key and then used it to decrypt the above ciphertext.



 



### Password
nuupjzigjv


