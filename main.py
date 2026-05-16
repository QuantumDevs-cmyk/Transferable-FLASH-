# ============================================================
# 🚀 Transferable Flash USDT
# ============================================================

SUPPORTED_NETWORKS = [
    "TRC20",
    "ERC20",
    "BEP20",
    "Fantom"
]

SUPPORTED_WALLETS = [
    "Trust Wallet",
    "MetaMask",
    "Exodus",
    "Ledger"
]

FEATURES = {
    "Fast Transactions": True,
    "Multi-Wallet Support": True,
    "Cross-Chain Compatibility": True,
    "Low Fees": True
}


def show_info():
    print("🚀 Transferable Flash USDT")
    print("Fast • Multi-Network • Secure Crypto Transfers")

    print("\n🌐 Supported Networks:")
    for network in SUPPORTED_NETWORKS:
        print(f"- {network}")

    print("\n💼 Supported Wallets:")
    for wallet in SUPPORTED_WALLETS:
        print(f"- {wallet}")

    print("\n⚡ Features:")
    for feature, enabled in FEATURES.items():
        print(f"- {feature}: {enabled}")


if __name__ == "__main__":
    show_info()
