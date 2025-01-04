from_src.democracy.proposal_manager_import_ProposalManager  class_SwarmVoting: """Handles_proposal_creation_and_voting_within_the_swarm."""  def___init__(self,_agents): self.agents_=_agents self.proposal_manager_=_ProposalManager()  def_create_and_vote(self,_description,_expiration_time): """Create_a_proposal_and_initiate_voting.""" proposal_id_=_f"proposal-{len(self.proposal_manager.proposals)_+_1}" Randomly_select_an_agent_to_create_the_proposal creator_agent_=_self.agents[0]___Example:_first_agent_creates_the_proposal creator_agent.create_proposal(self.proposal_manager,_proposal_id,_description,_expiration_time)  All_agents_vote_on_the_proposal for_agent_in_self.agents: vote_=_agent.decide_vote(proposal_id) self.proposal_manager.vote(proposal_id,_vote)  Check_and_return_the_results results_=_self.proposal_manager.check_results(proposal_id) return_results