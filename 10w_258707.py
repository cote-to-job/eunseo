def solution(coin, cards): 
    round = 1
    n = len(cards)
    card_dec = cards[: n // 3]
    card_round = set()
    offer = n+1
    for i in range(n // 3, n, 2):
        #카드 2장 추가
        card_round.add(cards[i])
        card_round.add(cards[i + 1])
        next_r = False #라운드 통과 가능 여부
        for d in card_dec:
            if offer - d in card_dec: # 기존카드 2장
                card_dec.remove(d)
                card_dec.remove(offer - d)

                next_r = True
                break
            elif offer - d in card_round: #새로운카드 1장 +기존카드 1장
                if coin:
                    coin -= 1
                    card_round.remove(offer - d)
                    card_dec.remove(d)
                    next_r = True
                    break
        if not next_r and coin >=2: #새로운 카드 2장
            for r in card_round:
                if offer - r in card_round:
                    coin -= 2
                    card_round.remove(r)
                    card_round.remove(offer - r)
                    next_r = True
                    break
        if not next_r: break
        round += 1

    return round 
