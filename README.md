# _mikro_-BRUTUS

PoC (Proof of Concept) Bruteforcing Utility RouterOS v6.48.6

_Mikro-BRUTUS_ is a simple proof of concept dictionary and blind brute forcing tool targeting the MikroTik RouterOS 6.x web interface. RouterOS notiously lacks brute force protections on the web and winbox interfaces. They've largely coasted off their custom authentication/encryption schemes from preventing these attacks.

Luckily [Margin Research](https://margin.re/2022/06/pulling-mikrotik-into-the-limelight/) released a python library that can handle authentication from 6.34 - 6.49.8 (current release).

This was written in about 10 minutes, and only to prove that MikroTik hasn't implemented any protections on the web interface.

## DEMO

Below is **Mikro-Brutus** in Action :

![Demo Animation](Mikro-Brutus.gif)

## Example Usage

```sh
git clone https://github.com/oyi77/mikro-brutus.git
cd mikro-brutus
python3 -m pip install -r requirements.txt
python3 bruteme.py --rhost 10.9.49.1 --username admin
Attempt 201
Success! Valid credentials:
admin:1qazxsw2
```

## Credit

- Margin Research - webfig.py is their work (with one tweak). The original can be found [here](https://github.com/MarginResearch/FOISted/blob/master/webfig.py).

- Bruteforce Dictionary - dictionary.txt is forked from the original leaked password dict. That can be found in the [here](http://downloads.skullsecurity.org/passwords/rockyou.txt.bz2).
