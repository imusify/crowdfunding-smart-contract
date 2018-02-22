Example addresses:

    AW5C5LZjyr1jBQuZZg3kAmmri6ic32yH2q    b'\x9c\xd87)\x13\xd6\xec\xb2hjWX\x89\x82\x15\xc3\x02\x8f\xc8m'
    AaLCDGQMuKdpNCkSVWVLry8MyvaXhbAXGW    b'\xcb\x8f\x12w\xb0e\xdb\xbaR\xe2\xb8\xaat\xfa@P(\xe7k:'

Build & test the contract

    neo> build imusc/ico_template.py test 0710 05 True False crowdfunding_create ["AJWvenTD6n7ya56AuiKS83oj36zCD65aqX", "AW5C5LZjyr1jBQuZZg3kAmmri6ic32yH2q", "AaLCDGQMuKdpNCkSVWVLry8MyvaXhbAXGW"]
    neo> build imusc/ico_template.py test 0710 05 True False crowdfunding_test ["AJWvenTD6n7ya56AuiKS83oj36zCD65aqX"]

Import to the blockchain

    import contract imusc/ico_template.avm 0710 05 True False

get hash (eg. 95ed79af690e274ad6c5594c4496daf72f5832b6)

Deploy

    testinvoke 95ed79af690e274ad6c5594c4496daf72f5832b6 deploy []
    testinvoke 95ed79af690e274ad6c5594c4496daf72f5832b6 circulation []

Mint some tokens

    testinvoke 95ed79af690e274ad6c5594c4496daf72f5832b6 mintTokens [] --attach-neo=1
    testinvoke 95ed79af690e274ad6c5594c4496daf72f5832b6 balanceOf ["AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y"]

Import token to neo-python wallet

    import token 95ed79af690e274ad6c5594c4496daf72f5832b6

----

Create a new crowdfunding address (AJWvenTD6n7ya56AuiKS83oj36zCD65aqX) with 2 members:

    testinvoke 95ed79af690e274ad6c5594c4496daf72f5832b6 crowdfunding_create ["AJWvenTD6n7ya56AuiKS83oj36zCD65aqX", "AW5C5LZjyr1jBQuZZg3kAmmri6ic32yH2q", "AaLCDGQMuKdpNCkSVWVLry8MyvaXhbAXGW"]

Check balances

    testinvoke 95ed79af690e274ad6c5594c4496daf72f5832b6 balanceOf ["AJWvenTD6n7ya56AuiKS83oj36zCD65aqX"]
    testinvoke 95ed79af690e274ad6c5594c4496daf72f5832b6 balanceOf ["AW5C5LZjyr1jBQuZZg3kAmmri6ic32yH2q"]
    testinvoke 95ed79af690e274ad6c5594c4496daf72f5832b6 balanceOf ["AaLCDGQMuKdpNCkSVWVLry8MyvaXhbAXGW"]

Get crowdfunding total contributions

    testinvoke 95ed79af690e274ad6c5594c4496daf72f5832b6 crowdfunding_total ["AJWvenTD6n7ya56AuiKS83oj36zCD65aqX"]

Test

    testinvoke 95ed79af690e274ad6c5594c4496daf72f5832b6 crowdfunding_test ["AJWvenTD6n7ya56AuiKS83oj36zCD65aqX"]

Send funds to the crowdfunding address

    send IMU AJWvenTD6n7ya56AuiKS83oj36zCD65aqX 200 --from-addr=AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y
