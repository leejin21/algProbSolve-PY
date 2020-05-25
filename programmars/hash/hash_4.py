# 베스트앨범
# 완료: O(nlogn)


def solution(genres, plays):
    playlist = dict()
    for g in genres:
        playlist[g] = [[], 0]

    for i in range(len(plays)):
        playlist[genres[i]][0].append(i)
        playlist[genres[i]][1] += plays[i]

    playlist = sorted(playlist.items(),
                      key=lambda item: item[1][1], reverse=True)

    sor_pl = [items[1][0] for items in playlist]
    ans = []
    for songs in sor_pl:
        songs = sorted(songs, key=lambda x: plays[x], reverse=True)
        ans += songs[:2]

    return ans


genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [800, 600, 800, 800, 2500]
print(solution(genres, plays))
