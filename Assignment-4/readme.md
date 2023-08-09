
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


<img width="744" alt="Screenshot 2023-08-10 at 03 09 17" src="https://github.com/sudikshanavik/CS641A/assets/100257642/cfa22ee5-93c7-42ba-9f36-ed477f7a53c2">

 <img width="744" alt="Screenshot 2023-08-10 at 03 09 28" src="https://github.com/sudikshanavik/CS641A/assets/100257642/d998d8aa-4163-4108-abb9-c1500f6d3562">

<img width="744" alt="Screenshot 2023-08-10 at 03 09 42" src="https://github.com/sudikshanavik/CS641A/assets/100257642/febedbaa-ce02-4d7c-a869-ed8d7856bac0">
<img width="744" alt="Screenshot 2023-08-10 at 03 09 57" src="https://github.com/sudikshanavik/CS641A/assets/100257642/653e6f68-d26e-441a-b299-88b1d3113038">
<img width="744" alt="Screenshot 2023-08-10 at 03 10 11" src="https://github.com/sudikshanavik/CS641A/assets/100257642/9a289b87-4037-4c5f-b53a-9eb4360e05aa">



### Password
nuupjzigjv


