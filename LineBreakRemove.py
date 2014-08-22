import sublime, sublime_plugin

class LineCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		s = self.view.sel()
		for region in s:
			if not region.empty():

				selection = self.view.substr(region)
				selection_mod = selection.replace('\n', ' ').replace('\r', '')
				selection_mod = " ".join(selection_mod.split())
			
				#self.view.insert(edit, 0, selection_mod)	
				sublime.set_clipboard(selection_mod)
				sublime.status_message("Selection with removed 'New Line Chars' copied to clipboard")
				#sublime.message_dialog("\"" + selection_mod +"\"" + "copied to clipboard")

		