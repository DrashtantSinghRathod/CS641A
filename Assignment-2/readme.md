# Level-2
## Vigenere Cipher
### Commands used in the game to reach the first ciphertext
+  go
+   back
+   read


### Cryptosystem was used at this level
Vigenere Cipher with the keyword: JCJCFFCCCB.

### Ciphertext Space:
Lg ccud qh urg tgay ejbwdkt, wmgtf su bgud nkudnk lrd vjfbg. 
	Yrhfm qvd vng sfuuxytj "vkj_ecwo_ogp_ej_rnfkukf" wt iq urtuwjm. 
	Ocz iqa jdag vio uzthsivi pqx vkj pgyd encpggt. Uy hopg yjg fhkz
	arz hkscv ckoq pgfn vu wwygt nkioe zttft djkth.

### Plaintext Space:
Be wary of the next chamber, there is very little joy there. Speak out the password "the_cave_man_be_pleased" to go through.May you have the strength for the next chamber. To find the exit, you first will need to utter magic words there.

### Observations used to figure out the cryptosystem
 After carefully observing the ciphertext, one thing we could conclude was that the cipher was only a plain monoalphabetic substitution cipher as it had words like "nnyvng" i.e. words starting with same letters, which does not happen in english. So, the cipher was most likely a polyalphabetic substitution cipher in which one letter in plaintext can be mapped to multiple letters in the ciphertext.

Also we observed from the vocabulary of this "Game" , the words "Chamber" , "Cave", "Password" etc. are very frequent. So, it is most likely the case that any seven-lettered word and eight-lettered word in the ciphertext could be "Chamber" and "Password" respectively. Note that these conclusions can be really helpful in actually decrypting the key and ultimately decrypting the entire ciphertext.

We got the clue from the first stage of the second level that the keyword length and the keyword letters of the used encryption system is "JCJCFFCCCB" as we observed the number of lines in the horizontal dimension in the face of the keeper which were 9, 2, 9, 2, 5, 5, 2, 2, 2, 1 . A famous example of polyalphabetic substitution cipher is Vigenere Cipher. So we started moving ahead with it.

We have the keyword for deciphering the ciphertext. For generating key, the given keyword is repeated in a circular manner until it matches the length of the ciphertext.

Keyword: JCJCFFCCCB


### Mapping

Encryption:
The plaintext(P) and key(K) are added modulo 26.
Ei = (Pi + Ki) mod 26

Decryption:
Di = (Ei - Ki + 26) mod 26
 



### Password
the_cave_man_be_pleased

