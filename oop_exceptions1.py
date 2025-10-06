'''
Exceptions. Task 1 
Implement a Pagination class helpful to arrange text on pages and list content on the given page. The class should take in a text and a positive integer
which indicate how many symbols will be allowed per page (take spaces into account as well). 
You need to be able to get the number of whole symbols in the text, get the number of pages that came out and the method that accepts the page
number, and return the number of symbols on this page. If the provided number of the page is missing raise exception with message “Invalid index. Page
is missing”. 
Implement searching/filtering pages by symbols/words and displaying pages with all the symbols on it. If the provided symbols/words are missing raise
exception with message “‘’ is missing on the pages”. 
If you’re querying by symbol that appears on many pages or if you are querying by the word that is splitted in two return an array of all the occurences. 
Pages indexing starts with 0. 
Example: ```python  pages = Pagination(‘Your beautiful text’, 5) pages.page_count 4 pages.item_count 19 
pages.count_items_on_page(0) 5 pages.count_items_on_page(3) 4 pages.count_items_on_page(4) Exception:
Invalid index. Page is missing. pages.find_page(‘Your’) [0] pages.find_page(‘e’) [1, 3] pages.find_page(‘beautiful’)
[1, 2] pages.find_page(‘great’) Exception: ‘great’ is missing on the pages pages.display_page(0) ‘Your ’ ``
'''
class Pagination:
    def __init__(self, data, items_on_page: int):
        if items_on_page <= 0:
            raise ValueError("Items per page must be positive")
        self.data = data
        self.items_on_page = items_on_page
        self.pages = [
            data[i:i + items_on_page]
            for i in range(0, len(data), items_on_page)
        ]

    @property
    def item_count(self):
        return len(self.data)

    @property
    def page_count(self):
        return len(self.pages)

    def count_items_on_page(self, page_number: int) -> int:
        if page_number < 0 or page_number >= self.page_count:
            raise Exception("Invalid index. Page is missing")
        return len(self.pages[page_number])

    def display_page(self, page_number: int) -> str:
        if page_number < 0 or page_number >= self.page_count:
            raise Exception("Invalid index. Page is missing")
        return self.pages[page_number]

    def find_page(self, query: str):
        found_pages = set()
        for i, page in enumerate(self.pages):
            # direct match inside the page
            if query in page:
                found_pages.add(i)
            # spanning check (page + next page)
            if i < self.page_count - 1:
                combined = page + self.pages[i + 1]
                if query in combined and query not in page and query not in self.pages[i + 1]:
                    found_pages.add(i)
                    found_pages.add(i + 1)

        if not found_pages:
            raise Exception(f"'{query}' is missing on the pages")

        return sorted(found_pages)
