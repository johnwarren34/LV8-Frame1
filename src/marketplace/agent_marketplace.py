class_AgentMarketplace: def___init__(self): self.market_=_[]  def_list_resource(self,_agent_id,_resource,_price): """List_a_resource_on_the_marketplace.""" self.market.append({"agent_id":_agent_id,_"resource":_resource,_"price":_price}) print(f"Agent_{agent_id}_listed_{resource}_for_{price}_credits.")  def_buy_resource(self,_buyer_id,_resource,_max_price): """Buy_a_resource_if_available_and_within_the_budget.""" for_listing_in_self.market: if_listing["resource"]_==_resource_and_listing["price"]_<=_max_price: print(f"Agent_{buyer_id}_bought_{resource}_from_Agent_{listing['agent_id']}_for_{listing['price']}_credits.") self.market.remove(listing) return_True print(f"Agent_{buyer_id}_could_not_buy_{resource}.") return_False  Example_usage if___name___==_"__main__": marketplace_=_AgentMarketplace() marketplace.list_resource(1,_"Energy",_10) marketplace.list_resource(2,_"Data",_15) marketplace.buy_resource(3,_"Energy",_12) marketplace.buy_resource(3,_"Data",_10)