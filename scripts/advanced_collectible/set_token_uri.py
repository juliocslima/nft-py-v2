from brownie import network, AdvancedCollectible
from scripts.helpful_scripts import get_account, OPENSEA_FORMAT, get_breed

dog_metadata_dic = {
    "PUG": "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmdryoExpgEQQQgJPoruwGJyZmz6SqV4FRTX1i73CT3iXn?filename=1-SHIBA_INU.json",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmbBnUjyHHN7Ytq9xDsYF9sucZdDJLRkWz7vnZfrjMXMxs?filename=2-ST_BERNARD.json",
}


def main():
    print(f"Working on {network.show_active()}")
    advanced_collectible = AdvancedCollectible[-1]
    number_of_collectible = advanced_collectible.tokenCounter()
    print(f"You have {number_of_collectible} tokens ID")

    for token_id in range(number_of_collectible):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        if not advanced_collectible.tokenURI(token_id).startswith("https://"):
            print(f"Setting token URI of {token_id}")
            set_token_uri(token_id, advanced_collectible,
                          dog_metadata_dic[breed])


def set_token_uri(token_id, nft_contract, token_uri):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id, token_uri, {"from": account})
    tx.wait(1)
    print(
        f"Awsome! You can view your NFT at {OPENSEA_FORMAT.format(nft_contract.address, token_id)}"
    )
    print("Please wait up to 20 minutes, and hit the refresh metadata button.")
