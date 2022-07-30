from io import StringIO
from unidiff import PatchSet

class DiffPackages:
    def __init__(self, packages) -> None:
        self.new_packages = packages
        self.upated_packages = packages
        self.removed_packages = packages

    @staticmethod
    def parse(diff: str, lock_file: str) -> 'DiffPackages':
        patch_set = PatchSet(StringIO(diff))

        change_list = []  

        lines_lock = lock_file.splitlines()

        for patched_file in patch_set:
            if 'poetry.lock' in patched_file.path:
                del_line_no = [line.target_line_no 
                            for hunk in patched_file for line in hunk 
                            if line.is_added and
                            line.value.strip() != ''] 
                ad_line_no = [line.source_line_no for hunk in patched_file 
                            for line in hunk if line.is_removed and
                            line.value.strip() != ''] 
            change_list.append((del_line_no, ad_line_no))
        packages = DiffPackages(change_list)
        return packages
