def is_valid(s: str) -> bool:
		choices = {
				"{":"}",
				"(":")",
				"[":"]"
		}
		o = []
		for (idx, val) in enumerate(s):
			if o:
				li = o[-1]
				if li in choices and choices[li] == val:
					o.pop()
				else:
					o.append(val)
			else:
				o.append(val)


		return len(o) == 0
        

