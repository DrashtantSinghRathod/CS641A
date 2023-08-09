
# Level-3
## Monoalphabetic Substitution and Permutation Cipher 
### Commands used in the game to reach the first ciphertext
+  go
+   enter
+   pluck
+   back
+   give
+   back
+   back
+   thrnxxtzy
+   read


### Cryptosystem was used at this level
Monoalphabetic Substitution and Permutation Cipher with block length=5
(1, 2, 3, 4, 5) --> (4, 3, 5, 1, 2)

### Ciphertext Space:
qmnjvsa nv wewc flct vprj tj tvvplvl fv xja vqildhc
	xmlnvc nacyclpa fc gyt vfvw. fv wgqyp, pqq pqcs y wsq
	rx qmnjvafy cgv tlvhf cw tyl aeuq fv xja tkbv cqnsqs. 
	lhf avawnc cv eas fuqb qvq tc yllrqr xxwa cfy. psdc uqf
	avrqc gefq pyat trac xwv taa wwd dv eas flcbq. vd trawm
	vupq quw x decgqcwt, yq yafl vlqs yqklhq! snafq vml
	lhvqpawr nqg_vfusr_ec_wawy qp fn wgawdgf.




### Observations used to figure out the cryptosystem
 With the help of 'give' command, we gave the mushrooms to the squeaky spirit and he gave gave us the magic word "thrnxxtzy". Using this spell on the main door, we got the ciphertext.

1) We analysed the ciphertext and it contained words like "xxwa", "wwd" which meant it could not be a plain substitution/caesar cipher.

2) We tried transposing the letters within the words but it didn't make sense at all.

3) We thought it could be Hill Cipher as the ciphertext consisted of repeating digraphs like "fv" which occurred thrice. So we tried out Hill Cipher with the size matrix= 2*2. But on generating all the possible decrypted texts by bruteforcing over all the matrices, the text didn't sense neither did it contained familiar words matching with the theme of this game such as password, caves etc.

4) We came across rail fence cipher which is a permutation cipher and used the lengths from 2 to 10 but the decrypted text did not make any sense.

5) We thought this time too the encryption might be done with the help of vigenere cipher as in the previous level. So we tried combinations of Vigenere Cipher and Hill Cipher. This time we used the key "thrnxxtzy" for the Vigenere Cipher which was the magic spell that we received in earlier part of this particular level. But the decrypted text didn't make much sense.

6) Finally we tried the substitution permutation/transposition technique as this technique is pretty common in block ciphers. We tried out a scheme in which the letters were substituted in a particular scheme and then were permuted in blocks of a fixed particular length. 

Analysis of the ciphertext with Substitution Permutation Cipher:

The length of the given ciphertext was 284.

As we divided the ciphertext into blocks of five, we saw some repetitive blocks such as "qmnjv", "fvxja", "veasf" which indicated that the block length could be actually equal to five.

We did try block lengths of four but didn't see such results. We skipped block lengths of two and three as they would lack security.

We tried the block length of 5. We first observed the last line of the ciphertext after the exclamation mark. With our experience of the previous assignments, we were pretty sure that "nqg_vfusr_ec_wawy" is the encrypted password. We were also able to guess that the words before this encrypted text are "speak the password", again from our previous experiences with every decryption level of this game. 

We broke the ciphertext into blocks of length five and found:   
Ciphertext            Plaintext
afqvm           ->     eakth
llhvq             ->      epass

1) We deduce, 'l' is is mapped to 's'  and the letters at positions 4 and 5 were permuted to 2, 1 (either case is possible). 

2) In the both ciphertext blocks, we have the letters 'v' and 'q'. So there possible mappings 'e' and 'a' (either case is possible). 

3) In both the plaintext blocks, 'e' is at position 1 and its possible mapping in the ciphertext could be 'v' and 'q' from the above point. In the corresponding ciphertext  the letter 'v' doesn't change its position but 'q' does. 'e' in plaintext could not be 'q'. So 'e' in plaintext is mapped to 'v' in ciphertext and 'a' in plaintext is mapped to 'q' in ciphertext. Also position 1 will be permuted to position 4. In the Plaintext-Ciphertext pair (eakth-afqvm), The letter 'a' which was at position 2 was and 'q' was at position 3 so position 2 was permuted to position 3. In the Plaintext-Ciphertext pair (epass-llhvq), The letter 'a' which was at position 3 was and 'q' was at position 5 so position 3 was permuted to position 5.

Similarly, by following the same procedure we deduced that the position 4 was permuted to position 2 and the position 5 was permuted to position 1.

Therefore, permutations:  (1, 2, 3, 4, 5) --> (4, 3, 5, 2, 1)

On further observing the above plaintext-ciphertext pair by the found permutation mapping, we found 'p','k' in plaintext is mapped to 'h','m' in ciphertext respectively,and 't','h' in plaintext is mapped to 'a','f' in ciphertext (either case might be true).

Now, we targeted those words in the ciphertext that contained the words with known mapping (l, h, v, q, a, f, m) in majority. The block "vtlvh" is mapped to "espel", from this pair, we deduced 't' is mapped to 'l'.


### Mapping

Ciphertext             Plaintext <br>
       l             ->             s<br>
       v            ->            e  <br>
      q              ->           a  <br>
       a            ->            t   <br>
        y           ->           n  <br>
        p            ->           d <br>
        w           ->           o  <br>
        t             ->            l <br>
        n            ->            r <br>
       c              ->            i<br>
      h               ->           p <br>
       s              ->            f <br>
       r              ->           w <br>
       x              ->           y  <br>
       d              ->          u   <br>
       b              ->          v   <br>
      u               ->          m   <br>
       m             ->           k  <br>
         f            ->             h<br>
       g              ->           g  <br>
       e              ->           c   <br>
       j              ->            b<br>
        i             ->           q<br>
       k              ->          not known (could be j/x/y) <br>
         
z and o didn't occur in the ciphertext text .<br>

No Digits occur in the ciphertext, so there mappings cannot be known.<br>

Punctuation marks were mapped to themselves.<br>
Underscore was mapped to itself.<br>

   ". "      ->     ". "<br>
   "_"      ->     "_  "<br>
   " ,"      ->     ",  "<br>
   "! "      ->     "! "<br>
 



### Password
the_magic_of_wand

