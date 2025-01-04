from_solana.rpc.api_import_Client from_solana.transaction_import_Transaction from_solana.publickey_import_PublicKey from_solana.keypair_import_Keypair from_solana.system_program_import_transfer,_TransferParams from_solana.rpc.types_import_TxOpts  class_SolanaUtils: """Utility_class_for_interacting_with_the_Solana_blockchain."""  def___init__(self,_rpc_url="https://api.mainnet-beta.solana.com"): self.client_=_Client(rpc_url)  def_get_balance(self,_public_key): """Get_the_balance_of_a_Solana_account.""" balance_=_self.client.get_balance(public_key) return_balance["result"]["value"]  def_send_transaction(self,_sender_keypair,_recipient_pubkey,_amount): """Send_SOL_from_one_account_to_another.""" transaction_=_Transaction().add( transfer( TransferParams( from_pubkey=sender_keypair.public_key, to_pubkey=PublicKey(recipient_pubkey), lamports=amount, ) ) ) response_=_self.client.send_transaction( transaction,_sender_keypair,_opts=TxOpts(skip_preflight=True) ) return_response["result"]  def_deploy_program(self,_sender_keypair,_program_path): """Deploy_a_Solana_smart_contract_(BPF_program).""" with_open(program_path,_"rb")_as_program_file: program_data_=_program_file.read() transaction_=_Transaction() transaction.add( self.client.request_airdrop(sender_keypair.public_key,_1_000_000_000) )___Add_lamports_for_deployment response_=_self.client.send_transaction( transaction,_sender_keypair,_opts=TxOpts(skip_preflight=True) ) return_response["result"]