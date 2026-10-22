class WorkflowService:
	WORKFLOW = ["Reviewer","Manager","Approver"]
	FINAL_STATUS = "Approved"
	@classmethod
	def get_next_role(cls, current_role):
		try:
			index = cls.WORKFLOW.index(current_role)
			if index == len(cls.WORKFLOW) - 1:
				return None
			return cls.WORKFLOW[index + 1]
		except ValueError:
			return None
	@classmethod
	def is_final_approver(cls,role):
		return role == cls.WORKFLOW[-1]