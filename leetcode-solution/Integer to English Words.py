class Solution:

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        # Lookup arrays for numbers
        LESS_THAN_20 = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        TENS = [
            "",
            "Ten",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]
        THOUSANDS = ["", "Thousand", "Million", "Billion"]

        # Helper function to process numbers less than 1000
        def helper(n: int) -> str:
            if n == 0:
                return ""
            elif n < 20:
                return LESS_THAN_20[n] + " "
            elif n < 100:
                return TENS[n // 10] + " " + helper(n % 10)
            else:
                return LESS_THAN_20[n // 100] + " Hundred " + helper(n % 100)

        res = ""
        i = 0

        # Process the number in chunks of 3 digits from right to left
        while num > 0:
            if num % 1000 != 0:
                res = helper(num % 1000) + THOUSANDS[i] + " " + res
            num //= 1000
            i += 1

        return res.strip()
