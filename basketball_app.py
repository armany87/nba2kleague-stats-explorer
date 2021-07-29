import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import json

st.title('NBA 2K League Player Stats Explorer')

st.markdown("""
This app performs simple webscraping of NBA 2K League player stats data!
* **Python libraries:** base64, pandas, streamlit
* **Data source:** [NBA 2K League Website](https://2kleague.nba.com/stats/).
""")

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(2018,2022))))

# Web scraping of NBA 2K League player stats
@st.cache
def load_data(year):
    url = "https://data.nba.com/data/10s/v2015/json/mobile_teams/2KL/2021/league/stats/12_league_leaders_points_02.json"
    html = pd.read_html(url, header = 0)
    df = html[0]
   
<div class="league-leaders__season-type">

                    <div class="league-leaders__stats-wrapper">
                        <div>
                            <div>
                                <h2>
                                    Points
                                </h2>
                                <!-- ngIf: lls.length == 0 -->
                            </div>
                        </div>

                        <!-- ngIf: lls.pl.length > 0 --><div ng-if="lls.pl.length > 0 " class="">
                            <table class="stats-table_page_league-leaders stats-table">
                                <thead>
                                    <tr>
                                        <th data-field="RANK">#</th>
                                        <th data-field="PLAYER">Player</th>
                                        <th data-field="TEAM">Team</th>
                                        <th data-field="PTS">PTS</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <!-- ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>1</td>
                                        <td>
                                            <a ng-href="/player/630/" href="/player/630/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630398.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630398.png">
                                                </div>
                                                <div class="player-handle">
                                                    630
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://pacersgaming.nba.com/" href="https://pacersgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/indiana.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/indiana.svg"><span class="team-name">Pacers Gaming</span></a></span>
                                        </td>
                                        <td>
                                            33.1
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>2</td>
                                        <td>
                                            <a ng-href="/player/splashy/" href="/player/splashy/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630055.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630055.png">
                                                </div>
                                                <div class="player-handle">
                                                    Splashy
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://jazzgaming.nba.com/" href="https://jazzgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/utah.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/utah.svg"><span class="team-name">Jazz Gaming</span></a></span>
                                        </td>
                                        <td>
                                            32.3
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>3</td>
                                        <td>
                                            <a ng-href="/player/bash/" href="/player/bash/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630062.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630062.png">
                                                </div>
                                                <div class="player-handle">
                                                    Bash
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://blazer5gaming.nba.com/" href="https://blazer5gaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/portland.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/portland.svg"><span class="team-name">Blazer5 Gaming</span></a></span>
                                        </td>
                                        <td>
                                            30.4
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>4</td>
                                        <td>
                                            <a ng-href="/player/choc/" href="/player/choc/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630054.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630054.png">
                                                </div>
                                                <div class="player-handle">
                                                    Choc
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://netsgc.nba.com/" href="https://netsgc.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/brooklyn.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/brooklyn.svg"><span class="team-name">NetsGC</span></a></span>
                                        </td>
                                        <td>
                                            29.2
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>5</td>
                                        <td>
                                            <a ng-href="/player/dre/" href="/player/dre/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630400.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    Dre
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://76ersgc.nba.com/" href="https://76ersgc.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/philadelphia.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/philadelphia.svg"><span class="team-name">76ers GC</span></a></span>
                                        </td>
                                        <td>
                                            27.2
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>6</td>
                                        <td>
                                            <a ng-href="/player/ofab/" href="/player/ofab/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600031.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600031.png">
                                                </div>
                                                <div class="player-handle">
                                                    oFAB
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://cavslegion.nba.com/" href="https://cavslegion.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/cleveland.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/cleveland.svg"><span class="team-name">Cavs Legion GC</span></a></span>
                                        </td>
                                        <td>
                                            27.0
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>7</td>
                                        <td>
                                            <a ng-href="/player/duck/" href="/player/duck/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630047.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    Duck
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://knicksgaming.nba.com/" href="https://knicksgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/new-york.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/new-york.svg"><span class="team-name">Knicks Gaming</span></a></span>
                                        </td>
                                        <td>
                                            26.9
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>8</td>
                                        <td>
                                            <a ng-href="/player/mama-im-dat-man/" href="/player/mama-im-dat-man/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600021.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600021.png">
                                                </div>
                                                <div class="player-handle">
                                                    Mama Im Dat Man
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://kingsguard.nba.com/" href="https://kingsguard.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/sacramento.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/sacramento.svg"><span class="team-name">Kings Guard Gaming</span></a></span>
                                        </td>
                                        <td>
                                            26.8
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>9</td>
                                        <td>
                                            <a ng-href="/player/greenlight/" href="/player/greenlight/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630413.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630413.png">
                                                </div>
                                                <div class="player-handle">
                                                    Greenlight
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://pistonsgt.nba.com/" href="https://pistonsgt.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/detroit.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/detroit.svg"><span class="team-name">Pistons GT</span></a></span>
                                        </td>
                                        <td>
                                            26.7
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>10</td>
                                        <td>
                                            <a ng-href="/player/radiant/" href="/player/radiant/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600097.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600097.png">
                                                </div>
                                                <div class="player-handle">
                                                    Radiant
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://pistonsgt.nba.com/" href="https://pistonsgt.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/detroit.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/detroit.svg"><span class="team-name">Pistons GT</span></a></span>
                                        </td>
                                        <td>
                                            26.1
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>11</td>
                                        <td>
                                            <a ng-href="/player/shiftykaii/" href="/player/shiftykaii/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630050.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630050.png">
                                                </div>
                                                <div class="player-handle">
                                                    ShiftyKaii
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://twolvesgaming.nba.com/" href="https://twolvesgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/minnesota.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/minnesota.svg"><span class="team-name">T-Wolves Gaming</span></a></span>
                                        </td>
                                        <td>
                                            25.9
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>12</td>
                                        <td>
                                            <a ng-href="/player/sav/" href="/player/sav/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630052.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630052.png">
                                                </div>
                                                <div class="player-handle">
                                                    SAV
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://heatcheck.nba.com/" href="https://heatcheck.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/miami.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/miami.svg"><span class="team-name">Heat Check Gaming</span></a></span>
                                        </td>
                                        <td>
                                            25.7
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>13</td>
                                        <td>
                                            <a ng-href="/player/ceez/" href="/player/ceez/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630406.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630406.png">
                                                </div>
                                                <div class="player-handle">
                                                    Ceez
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://hawkstalon.nba.com/" href="https://hawkstalon.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/atlanta.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/atlanta.svg"><span class="team-name">Hawks Talon GC</span></a></span>
                                        </td>
                                        <td>
                                            25.6
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>14</td>
                                        <td>
                                            <a ng-href="/player/vandi/" href="/player/vandi/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600249.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600249.png">
                                                </div>
                                                <div class="player-handle">
                                                    Vandi
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://grizzgaming.nba.com/" href="https://grizzgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/memphis.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/memphis.svg"><span class="team-name">Grizz Gaming</span></a></span>
                                        </td>
                                        <td>
                                            25.4
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>15</td>
                                        <td>
                                            <a ng-href="/player/regg/" href="/player/regg/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630056.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    Regg
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://bucksgaming.nba.com/" href="https://bucksgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/milwaukee.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/milwaukee.svg"><span class="team-name">Bucks Gaming</span></a></span>
                                        </td>
                                        <td>
                                            25.2
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>16</td>
                                        <td>
                                            <a ng-href="/player/dimez/" href="/player/dimez/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600004.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600004.png">
                                                </div>
                                                <div class="player-handle">
                                                    Dimez
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://raptorsuprising.nba.com/" href="https://raptorsuprising.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/toronto.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/toronto.svg"><span class="team-name">Raptors Uprising GC</span></a></span>
                                        </td>
                                        <td>
                                            24.7
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>17</td>
                                        <td>
                                            <a ng-href="/player/jbm/" href="/player/jbm/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630046.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630046.png">
                                                </div>
                                                <div class="player-handle">
                                                    JBM
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://wizardsdg.nba.com/" href="https://wizardsdg.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/washington.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/washington.svg"><span class="team-name">Wizards District Gaming</span></a></span>
                                        </td>
                                        <td>
                                            24.2
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>18</td>
                                        <td>
                                            <a ng-href="/player/reizey/" href="/player/reizey/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600217.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600217.png">
                                                </div>
                                                <div class="player-handle">
                                                    Reizey
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://magicgaming.nba.com/" href="https://magicgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/orlando.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/orlando.svg"><span class="team-name">Magic Gaming</span></a></span>
                                        </td>
                                        <td>
                                            22.8
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>19</td>
                                        <td>
                                            <a ng-href="/player/beardabeast/" href="/player/beardabeast/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600221.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600221.png">
                                                </div>
                                                <div class="player-handle">
                                                    BearDaBeast
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://twolvesgaming.nba.com/" href="https://twolvesgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/minnesota.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/minnesota.svg"><span class="team-name">T-Wolves Gaming</span></a></span>
                                        </td>
                                        <td>
                                            22.4
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>20</td>
                                        <td>
                                            <a ng-href="/player/kenny-got-work/" href="/player/kenny-got-work/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600017.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600017.png">
                                                </div>
                                                <div class="player-handle">
                                                    Kenny Got Work
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://raptorsuprising.nba.com/" href="https://raptorsuprising.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/toronto.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/toronto.svg"><span class="team-name">Raptors Uprising GC</span></a></span>
                                        </td>
                                        <td>
                                            22.4
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>21</td>
                                        <td>
                                            <a ng-href="/player/bsmoove/" href="/player/bsmoove/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600026.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600026.png">
                                                </div>
                                                <div class="player-handle">
                                                    Bsmoove
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://gengtigers.nba.com/" href="https://gengtigers.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/shanghai.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/shanghai.svg"><span class="team-name">Gen.G Tigers</span></a></span>
                                        </td>
                                        <td>
                                            22.4
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>22</td>
                                        <td>
                                            <a ng-href="/player/reesedagod/" href="/player/reesedagod/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600009.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600009.png">
                                                </div>
                                                <div class="player-handle">
                                                    ReeseDaGod
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://lakersgaming.nba.com/" href="https://lakersgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/losangeles.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/losangeles.svg"><span class="team-name">Lakers Gaming</span></a></span>
                                        </td>
                                        <td>
                                            22.3
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>23</td>
                                        <td>
                                            <a ng-href="/player/cb13/" href="/player/cb13/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600205.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600205.png">
                                                </div>
                                                <div class="player-handle">
                                                    CB13
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://warriorsgs.nba.com/" href="https://warriorsgs.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/golden-state.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/golden-state.svg"><span class="team-name">Warriors Gaming Squad</span></a></span>
                                        </td>
                                        <td>
                                            22.1
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>24</td>
                                        <td>
                                            <a ng-href="/player/sherm/" href="/player/sherm/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600243.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600243.png">
                                                </div>
                                                <div class="player-handle">
                                                    Sherm
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://hornetsvenomgt.nba.com/" href="https://hornetsvenomgt.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/charlotte.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/charlotte.svg"><span class="team-name">Hornets Venom GT</span></a></span>
                                        </td>
                                        <td>
                                            21.6
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>25</td>
                                        <td>
                                            <a ng-href="/player/rigby/" href="/player/rigby/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630403.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    rigby
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://hornetsvenomgt.nba.com/" href="https://hornetsvenomgt.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/charlotte.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/charlotte.svg"><span class="team-name">Hornets Venom GT</span></a></span>
                                        </td>
                                        <td>
                                            21.3
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>26</td>
                                        <td>
                                            <a ng-href="/player/jmoney/" href="/player/jmoney/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600228.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600228.png">
                                                </div>
                                                <div class="player-handle">
                                                    JMoney
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://gengtigers.nba.com/" href="https://gengtigers.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/shanghai.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/shanghai.svg"><span class="team-name">Gen.G Tigers</span></a></span>
                                        </td>
                                        <td>
                                            21.2
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>27</td>
                                        <td>
                                            <a ng-href="/player/originalmalik/" href="/player/originalmalik/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600218.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600218.png">
                                                </div>
                                                <div class="player-handle">
                                                    OriginalMalik
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://knicksgaming.nba.com/" href="https://knicksgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/new-york.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/new-york.svg"><span class="team-name">Knicks Gaming</span></a></span>
                                        </td>
                                        <td>
                                            21.1
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>28</td>
                                        <td>
                                            <a ng-href="/player/ft/" href="/player/ft/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630394.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    FT
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://celticscrossover.nba.com/" href="https://celticscrossover.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/boston.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/boston.svg"><span class="team-name">Celtics Crossover Gaming</span></a></span>
                                        </td>
                                        <td>
                                            20.3
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>29</td>
                                        <td>
                                            <a ng-href="/player/hotshot/" href="/player/hotshot/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600015.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600015.png">
                                                </div>
                                                <div class="player-handle">
                                                    Hotshot
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://heatcheck.nba.com/" href="https://heatcheck.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/miami.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/miami.svg"><span class="team-name">Heat Check Gaming</span></a></span>
                                        </td>
                                        <td>
                                            20.0
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>30</td>
                                        <td>
                                            <a ng-href="/player/shotz/" href="/player/shotz/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600028.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600028.png">
                                                </div>
                                                <div class="player-handle">
                                                    Shotz
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://netsgc.nba.com/" href="https://netsgc.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/brooklyn.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/brooklyn.svg"><span class="team-name">NetsGC</span></a></span>
                                        </td>
                                        <td>
                                            19.2
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>31</td>
                                        <td>
                                            <a ng-href="/player/hezi/" href="/player/hezi/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630399.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    Hezi
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://warriorsgs.nba.com/" href="https://warriorsgs.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/golden-state.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/golden-state.svg"><span class="team-name">Warriors Gaming Squad</span></a></span>
                                        </td>
                                        <td>
                                            18.9
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>32</td>
                                        <td>
                                            <a ng-href="/player/walkingbucket/" href="/player/walkingbucket/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630402.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    WalkingBucket
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://celticscrossover.nba.com/" href="https://celticscrossover.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/boston.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/boston.svg"><span class="team-name">Celtics Crossover Gaming</span></a></span>
                                        </td>
                                        <td>
                                            18.4
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>33</td>
                                        <td>
                                            <a ng-href="/player/onewildwalnut/" href="/player/onewildwalnut/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600011.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600011.png">
                                                </div>
                                                <div class="player-handle">
                                                    OneWildWalnut
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://76ersgc.nba.com/" href="https://76ersgc.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/philadelphia.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/philadelphia.svg"><span class="team-name">76ers GC</span></a></span>
                                        </td>
                                        <td>
                                            18.3
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>34</td>
                                        <td>
                                            <a ng-href="/player/dayfri/" href="/player/dayfri/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600060.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600060.png">
                                                </div>
                                                <div class="player-handle">
                                                    Dayfri
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://wizardsdg.nba.com/" href="https://wizardsdg.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/washington.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/washington.svg"><span class="team-name">Wizards District Gaming</span></a></span>
                                        </td>
                                        <td>
                                            17.7
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>35</td>
                                        <td>
                                            <a ng-href="/player/type/" href="/player/type/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600033.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600033.png">
                                                </div>
                                                <div class="player-handle">
                                                    Type
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://raptorsuprising.nba.com/" href="https://raptorsuprising.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/toronto.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/toronto.svg"><span class="team-name">Raptors Uprising GC</span></a></span>
                                        </td>
                                        <td>
                                            17.3
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>36</td>
                                        <td>
                                            <a ng-href="/player/feast/" href="/player/feast/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600039.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600039.png">
                                                </div>
                                                <div class="player-handle">
                                                    FEAST
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://gengtigers.nba.com/" href="https://gengtigers.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/shanghai.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/shanghai.svg"><span class="team-name">Gen.G Tigers</span></a></span>
                                        </td>
                                        <td>
                                            17.1
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>37</td>
                                        <td>
                                            <a ng-href="/player/strainer/" href="/player/strainer/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600230.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600230.png">
                                                </div>
                                                <div class="player-handle">
                                                    Strainer
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://cavslegion.nba.com/" href="https://cavslegion.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/cleveland.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/cleveland.svg"><span class="team-name">Cavs Legion GC</span></a></span>
                                        </td>
                                        <td>
                                            16.3
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>38</td>
                                        <td>
                                            <a ng-href="/player/ramo/" href="/player/ramo/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600042.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600042.png">
                                                </div>
                                                <div class="player-handle">
                                                    Ramo
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://pistonsgt.nba.com/" href="https://pistonsgt.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/detroit.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/detroit.svg"><span class="team-name">Pistons GT</span></a></span>
                                        </td>
                                        <td>
                                            15.9
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>39</td>
                                        <td>
                                            <a ng-href="/player/slaughter/" href="/player/slaughter/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600019.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600019.png">
                                                </div>
                                                <div class="player-handle">
                                                    Slaughter
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://twolvesgaming.nba.com/" href="https://twolvesgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/minnesota.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/minnesota.svg"><span class="team-name">T-Wolves Gaming</span></a></span>
                                        </td>
                                        <td>
                                            15.7
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>40</td>
                                        <td>
                                            <a ng-href="/player/plondo/" href="/player/plondo/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600224.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600224.png">
                                                </div>
                                                <div class="player-handle">
                                                    Plondo
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://bucksgaming.nba.com/" href="https://bucksgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/milwaukee.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/milwaukee.svg"><span class="team-name">Bucks Gaming</span></a></span>
                                        </td>
                                        <td>
                                            15.7
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>41</td>
                                        <td>
                                            <a ng-href="/player/snubby/" href="/player/snubby/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630063.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    Snubby
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://magicgaming.nba.com/" href="https://magicgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/orlando.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/orlando.svg"><span class="team-name">Magic Gaming</span></a></span>
                                        </td>
                                        <td>
                                            15.6
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>42</td>
                                        <td>
                                            <a ng-href="/player/bp/" href="/player/bp/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600209.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600209.png">
                                                </div>
                                                <div class="player-handle">
                                                    BP
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://hawkstalon.nba.com/" href="https://hawkstalon.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/atlanta.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/atlanta.svg"><span class="team-name">Hawks Talon GC</span></a></span>
                                        </td>
                                        <td>
                                            15.4
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>43</td>
                                        <td>
                                            <a ng-href="/player/petebeballin/" href="/player/petebeballin/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600226.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600226.png">
                                                </div>
                                                <div class="player-handle">
                                                    PeteBeBallin
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://hornetsvenomgt.nba.com/" href="https://hornetsvenomgt.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/charlotte.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/charlotte.svg"><span class="team-name">Hornets Venom GT</span></a></span>
                                        </td>
                                        <td>
                                            15.2
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>44</td>
                                        <td>
                                            <a ng-href="/player/krazy/" href="/player/krazy/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630397.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630397.png">
                                                </div>
                                                <div class="player-handle">
                                                    Krazy
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://lakersgaming.nba.com/" href="https://lakersgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/losangeles.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/losangeles.svg"><span class="team-name">Lakers Gaming</span></a></span>
                                        </td>
                                        <td>
                                            15.0
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>45</td>
                                        <td>
                                            <a ng-href="/player/arooks/" href="/player/arooks/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600043.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600043.png">
                                                </div>
                                                <div class="player-handle">
                                                    Arooks
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://76ersgc.nba.com/" href="https://76ersgc.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/philadelphia.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/philadelphia.svg"><span class="team-name">76ers GC</span></a></span>
                                        </td>
                                        <td>
                                            15.0
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>46</td>
                                        <td>
                                            <a ng-href="/player/bohio/" href="/player/bohio/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630049.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630049.png">
                                                </div>
                                                <div class="player-handle">
                                                    BOHIO
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://lakersgaming.nba.com/" href="https://lakersgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/losangeles.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/losangeles.svg"><span class="team-name">Lakers Gaming</span></a></span>
                                        </td>
                                        <td>
                                            14.4
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>47</td>
                                        <td>
                                            <a ng-href="/player/chess/" href="/player/chess/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630396.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    Chess
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://grizzgaming.nba.com/" href="https://grizzgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/memphis.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/memphis.svg"><span class="team-name">Grizz Gaming</span></a></span>
                                        </td>
                                        <td>
                                            14.3
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>48</td>
                                        <td>
                                            <a ng-href="/player/ria/" href="/player/ria/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600252.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600252.png">
                                                </div>
                                                <div class="player-handle">
                                                    Ria
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://jazzgaming.nba.com/" href="https://jazzgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/utah.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/utah.svg"><span class="team-name">Jazz Gaming</span></a></span>
                                        </td>
                                        <td>
                                            14.3
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>49</td>
                                        <td>
                                            <a ng-href="/player/sick-one/" href="/player/sick-one/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600040.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600040.png">
                                                </div>
                                                <div class="player-handle">
                                                    Sick One
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://mavsgaming.nba.com/" href="https://mavsgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/dallas.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/dallas.svg"><span class="team-name">Mavs Gaming</span></a></span>
                                        </td>
                                        <td>
                                            14.1
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>50</td>
                                        <td>
                                            <a ng-href="/player/gen/" href="/player/gen/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630076.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    Gen
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://mavsgaming.nba.com/" href="https://mavsgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/dallas.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/dallas.svg"><span class="team-name">Mavs Gaming</span></a></span>
                                        </td>
                                        <td>
                                            14.1
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>51</td>
                                        <td>
                                            <a ng-href="/player/may/" href="/player/may/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600229.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600229.png">
                                                </div>
                                                <div class="player-handle">
                                                    May
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://magicgaming.nba.com/" href="https://magicgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/orlando.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/orlando.svg"><span class="team-name">Magic Gaming</span></a></span>
                                        </td>
                                        <td>
                                            14.0
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>52</td>
                                        <td>
                                            <a ng-href="/player/dlaw/" href="/player/dlaw/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630410.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    DLAW
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://cavslegion.nba.com/" href="https://cavslegion.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/cleveland.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/cleveland.svg"><span class="team-name">Cavs Legion GC</span></a></span>
                                        </td>
                                        <td>
                                            13.8
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>53</td>
                                        <td>
                                            <a ng-href="/player/worthingcolt/" href="/player/worthingcolt/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600056.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600056.png">
                                                </div>
                                                <div class="player-handle">
                                                    worthingcolt
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://celticscrossover.nba.com/" href="https://celticscrossover.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/boston.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/boston.svg"><span class="team-name">Celtics Crossover Gaming</span></a></span>
                                        </td>
                                        <td>
                                            13.8
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>54</td>
                                        <td>
                                            <a ng-href="/player/expose/" href="/player/expose/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630051.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    Expose
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://bucksgaming.nba.com/" href="https://bucksgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/milwaukee.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/milwaukee.svg"><span class="team-name">Bucks Gaming</span></a></span>
                                        </td>
                                        <td>
                                            13.6
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>55</td>
                                        <td>
                                            <a ng-href="/player/authenticafrican/" href="/player/authenticafrican/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600053.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600053.png">
                                                </div>
                                                <div class="player-handle">
                                                    AuthenticAfrican
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://grizzgaming.nba.com/" href="https://grizzgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/memphis.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/memphis.svg"><span class="team-name">Grizz Gaming</span></a></span>
                                        </td>
                                        <td>
                                            13.5
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>56</td>
                                        <td>
                                            <a ng-href="/player/jomar/" href="/player/jomar/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600095.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600095.png">
                                                </div>
                                                <div class="player-handle">
                                                    Jomar
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://pacersgaming.nba.com/" href="https://pacersgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/indiana.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/indiana.svg"><span class="team-name">Pacers Gaming</span></a></span>
                                        </td>
                                        <td>
                                            13.4
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>57</td>
                                        <td>
                                            <a ng-href="/player/swizurk/" href="/player/swizurk/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600016.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600016.png">
                                                </div>
                                                <div class="player-handle">
                                                    Swizurk
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://pacersgaming.nba.com/" href="https://pacersgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/indiana.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/indiana.svg"><span class="team-name">Pacers Gaming</span></a></span>
                                        </td>
                                        <td>
                                            13.4
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>58</td>
                                        <td>
                                            <a ng-href="/player/antoine/" href="/player/antoine/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630408.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    ANTOINE
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://warriorsgs.nba.com/" href="https://warriorsgs.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/golden-state.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/golden-state.svg"><span class="team-name">Warriors Gaming Squad</span></a></span>
                                        </td>
                                        <td>
                                            12.9
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>59</td>
                                        <td>
                                            <a ng-href="/player/gradient/" href="/player/gradient/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600241.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600241.png">
                                                </div>
                                                <div class="player-handle">
                                                    Gradient
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://warriorsgs.nba.com/" href="https://warriorsgs.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/golden-state.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/golden-state.svg"><span class="team-name">Warriors Gaming Squad</span></a></span>
                                        </td>
                                        <td>
                                            12.4
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>60</td>
                                        <td>
                                            <a ng-href="/player/glo/" href="/player/glo/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630404.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    Glo
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://knicksgaming.nba.com/" href="https://knicksgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/new-york.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/new-york.svg"><span class="team-name">Knicks Gaming</span></a></span>
                                        </td>
                                        <td>
                                            12.3
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>61</td>
                                        <td>
                                            <a ng-href="/player/brich/" href="/player/brich/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630092.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    BRich
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://wizardsdg.nba.com/" href="https://wizardsdg.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/washington.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/washington.svg"><span class="team-name">Wizards District Gaming</span></a></span>
                                        </td>
                                        <td>
                                            12.2
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>62</td>
                                        <td>
                                            <a ng-href="/player/reecemode/" href="/player/reecemode/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630080.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    ReeceMode
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://mavsgaming.nba.com/" href="https://mavsgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/dallas.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/dallas.svg"><span class="team-name">Mavs Gaming</span></a></span>
                                        </td>
                                        <td>
                                            12.2
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>63</td>
                                        <td>
                                            <a ng-href="/player/seemo/" href="/player/seemo/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600093.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600093.png">
                                                </div>
                                                <div class="player-handle">
                                                    Seemo
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://kingsguard.nba.com/" href="https://kingsguard.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/sacramento.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/sacramento.svg"><span class="team-name">Kings Guard Gaming</span></a></span>
                                        </td>
                                        <td>
                                            12.1
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>64</td>
                                        <td>
                                            <a ng-href="/player/big-saint/" href="/player/big-saint/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630066.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    Big Saint
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://twolvesgaming.nba.com/" href="https://twolvesgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/minnesota.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/minnesota.svg"><span class="team-name">T-Wolves Gaming</span></a></span>
                                        </td>
                                        <td>
                                            12.1
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>65</td>
                                        <td>
                                            <a ng-href="/player/faiz/" href="/player/faiz/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630416.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    Faiz
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://netsgc.nba.com/" href="https://netsgc.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/brooklyn.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/brooklyn.svg"><span class="team-name">NetsGC</span></a></span>
                                        </td>
                                        <td>
                                            12.1
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>66</td>
                                        <td>
                                            <a ng-href="/player/scretty/" href="/player/scretty/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600025.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600025.png">
                                                </div>
                                                <div class="player-handle">
                                                    Scretty
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://blazer5gaming.nba.com/" href="https://blazer5gaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/portland.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/portland.svg"><span class="team-name">Blazer5 Gaming</span></a></span>
                                        </td>
                                        <td>
                                            12.1
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>67</td>
                                        <td>
                                            <a ng-href="/player/yusuf-scarbz/" href="/player/yusuf-scarbz/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600052.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600052.png">
                                                </div>
                                                <div class="player-handle">
                                                    Yusuf Scarbz
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://kingsguard.nba.com/" href="https://kingsguard.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/sacramento.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/sacramento.svg"><span class="team-name">Kings Guard Gaming</span></a></span>
                                        </td>
                                        <td>
                                            11.9
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>68</td>
                                        <td>
                                            <a ng-href="/player/g-o-o-f-y-7-5-7/" href="/player/g-o-o-f-y-7-5-7/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600007.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600007.png">
                                                </div>
                                                <div class="player-handle">
                                                    G O O F Y 7 5 7
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://blazer5gaming.nba.com/" href="https://blazer5gaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/portland.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/portland.svg"><span class="team-name">Blazer5 Gaming</span></a></span>
                                        </td>
                                        <td>
                                            11.6
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>69</td>
                                        <td>
                                            <a ng-href="/player/zae/" href="/player/zae/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630064.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    Zae
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://mavsgaming.nba.com/" href="https://mavsgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/dallas.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/dallas.svg"><span class="team-name">Mavs Gaming</span></a></span>
                                        </td>
                                        <td>
                                            11.4
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>70</td>
                                        <td>
                                            <a ng-href="/player/lee/" href="/player/lee/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630061.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630061.png">
                                                </div>
                                                <div class="player-handle">
                                                    Lee
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://hawkstalon.nba.com/" href="https://hawkstalon.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/atlanta.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/atlanta.svg"><span class="team-name">Hawks Talon GC</span></a></span>
                                        </td>
                                        <td>
                                            11.3
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>71</td>
                                        <td>
                                            <a ng-href="/player/crush/" href="/player/crush/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630048.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    Crush
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://kingsguard.nba.com/" href="https://kingsguard.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/sacramento.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/sacramento.svg"><span class="team-name">Kings Guard Gaming</span></a></span>
                                        </td>
                                        <td>
                                            10.8
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>72</td>
                                        <td>
                                            <a ng-href="/player/breadwinnerla/" href="/player/breadwinnerla/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600222.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600222.png">
                                                </div>
                                                <div class="player-handle">
                                                    BreadwinnerLA
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://blazer5gaming.nba.com/" href="https://blazer5gaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/portland.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/portland.svg"><span class="team-name">Blazer5 Gaming</span></a></span>
                                        </td>
                                        <td>
                                            10.7
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>73</td>
                                        <td>
                                            <a ng-href="/player/lotty/" href="/player/lotty/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600227.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600227.png">
                                                </div>
                                                <div class="player-handle">
                                                    Lotty
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://jazzgaming.nba.com/" href="https://jazzgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/utah.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/utah.svg"><span class="team-name">Jazz Gaming</span></a></span>
                                        </td>
                                        <td>
                                            10.3
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>74</td>
                                        <td>
                                            <a ng-href="/player/slayisland/" href="/player/slayisland/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600223.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600223.png">
                                                </div>
                                                <div class="player-handle">
                                                    SlayIsland
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://netsgc.nba.com/" href="https://netsgc.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/brooklyn.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/brooklyn.svg"><span class="team-name">NetsGC</span></a></span>
                                        </td>
                                        <td>
                                            10.1
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>75</td>
                                        <td>
                                            <a ng-href="/player/spartxn/" href="/player/spartxn/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630091.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    Spartxn
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://grizzgaming.nba.com/" href="https://grizzgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/memphis.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/memphis.svg"><span class="team-name">Grizz Gaming</span></a></span>
                                        </td>
                                        <td>
                                            9.9
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>76</td>
                                        <td>
                                            <a ng-href="/player/caliraq/" href="/player/caliraq/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630407.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    Caliraq
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://bucksgaming.nba.com/" href="https://bucksgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/milwaukee.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/milwaukee.svg"><span class="team-name">Bucks Gaming</span></a></span>
                                        </td>
                                        <td>
                                            9.9
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>77</td>
                                        <td>
                                            <a ng-href="/player/dt/" href="/player/dt/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600246.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600246.png">
                                                </div>
                                                <div class="player-handle">
                                                    DT
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://magicgaming.nba.com/" href="https://magicgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/orlando.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/orlando.svg"><span class="team-name">Magic Gaming</span></a></span>
                                        </td>
                                        <td>
                                            9.8
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>78</td>
                                        <td>
                                            <a ng-href="/player/majes7ic/" href="/player/majes7ic/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600047.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600047.png">
                                                </div>
                                                <div class="player-handle">
                                                    MaJes7ic
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://kingsguard.nba.com/" href="https://kingsguard.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/sacramento.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/sacramento.svg"><span class="team-name">Kings Guard Gaming</span></a></span>
                                        </td>
                                        <td>
                                            9.5
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>79</td>
                                        <td>
                                            <a ng-href="/player/newdini/" href="/player/newdini/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600022.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600022.png">
                                                </div>
                                                <div class="player-handle">
                                                    Newdini
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://wizardsdg.nba.com/" href="https://wizardsdg.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/washington.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/washington.svg"><span class="team-name">Wizards District Gaming</span></a></span>
                                        </td>
                                        <td>
                                            9.5
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>80</td>
                                        <td>
                                            <a ng-href="/player/lavishphenom/" href="/player/lavishphenom/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600049.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600049.png">
                                                </div>
                                                <div class="player-handle">
                                                    LavishPhenom
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://pacersgaming.nba.com/" href="https://pacersgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/indiana.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/indiana.svg"><span class="team-name">Pacers Gaming</span></a></span>
                                        </td>
                                        <td>
                                            9.4
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>81</td>
                                        <td>
                                            <a ng-href="/player/all-hail-trey/" href="/player/all-hail-trey/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600073.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600073.png">
                                                </div>
                                                <div class="player-handle">
                                                    All Hail Trey
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://raptorsuprising.nba.com/" href="https://raptorsuprising.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/toronto.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/toronto.svg"><span class="team-name">Raptors Uprising GC</span></a></span>
                                        </td>
                                        <td>
                                            9.3
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>82</td>
                                        <td>
                                            <a ng-href="/player/charger-x-704/" href="/player/charger-x-704/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630059.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    Charger x 704
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://pistonsgt.nba.com/" href="https://pistonsgt.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/detroit.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/detroit.svg"><span class="team-name">Pistons GT</span></a></span>
                                        </td>
                                        <td>
                                            8.9
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>83</td>
                                        <td>
                                            <a ng-href="/player/lord-beezus/" href="/player/lord-beezus/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600200.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600200.png">
                                                </div>
                                                <div class="player-handle">
                                                    Lord Beezus
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://jazzgaming.nba.com/" href="https://jazzgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/utah.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/utah.svg"><span class="team-name">Jazz Gaming</span></a></span>
                                        </td>
                                        <td>
                                            8.8
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>84</td>
                                        <td>
                                            <a ng-href="/player/tsjosh/" href="/player/tsjosh/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600079.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600079.png">
                                                </div>
                                                <div class="player-handle">
                                                    TsJosh
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://raptorsuprising.nba.com/" href="https://raptorsuprising.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/toronto.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/toronto.svg"><span class="team-name">Raptors Uprising GC</span></a></span>
                                        </td>
                                        <td>
                                            8.8
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>85</td>
                                        <td>
                                            <a ng-href="/player/dante/" href="/player/dante/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630433.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    Dante
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://netsgc.nba.com/" href="https://netsgc.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/brooklyn.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/brooklyn.svg"><span class="team-name">NetsGC</span></a></span>
                                        </td>
                                        <td>
                                            8.6
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>86</td>
                                        <td>
                                            <a ng-href="/player/myles/" href="/player/myles/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630427.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    Myles
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://twolvesgaming.nba.com/" href="https://twolvesgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/minnesota.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/minnesota.svg"><span class="team-name">T-Wolves Gaming</span></a></span>
                                        </td>
                                        <td>
                                            8.5
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>87</td>
                                        <td>
                                            <a ng-href="/player/seese/" href="/player/seese/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630419.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630419.png">
                                                </div>
                                                <div class="player-handle">
                                                    Seese
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://lakersgaming.nba.com/" href="https://lakersgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/losangeles.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/losangeles.svg"><span class="team-name">Lakers Gaming</span></a></span>
                                        </td>
                                        <td>
                                            8.3
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>88</td>
                                        <td>
                                            <a ng-href="/player/wolf/" href="/player/wolf/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600038.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600038.png">
                                                </div>
                                                <div class="player-handle">
                                                    WoLF
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://pacersgaming.nba.com/" href="https://pacersgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/indiana.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/indiana.svg"><span class="team-name">Pacers Gaming</span></a></span>
                                        </td>
                                        <td>
                                            8.1
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>89</td>
                                        <td>
                                            <a ng-href="/player/futureclutch/" href="/player/futureclutch/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630415.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    FutureClutch
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://magicgaming.nba.com/" href="https://magicgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/orlando.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/orlando.svg"><span class="team-name">Magic Gaming</span></a></span>
                                        </td>
                                        <td>
                                            8.0
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>89</td>
                                        <td>
                                            <a ng-href="/player/big-perm/" href="/player/big-perm/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630431.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    Big Perm
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://bucksgaming.nba.com/" href="https://bucksgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/milwaukee.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/milwaukee.svg"><span class="team-name">Bucks Gaming</span></a></span>
                                        </td>
                                        <td>
                                            8.0
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>91</td>
                                        <td>
                                            <a ng-href="/player/trap/" href="/player/trap/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630071.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    Trap
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://hornetsvenomgt.nba.com/" href="https://hornetsvenomgt.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/charlotte.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/charlotte.svg"><span class="team-name">Hornets Venom GT</span></a></span>
                                        </td>
                                        <td>
                                            7.9
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>92</td>
                                        <td>
                                            <a ng-href="/player/tactuk/" href="/player/tactuk/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630067.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630067.png">
                                                </div>
                                                <div class="player-handle">
                                                    Tactuk
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://lakersgaming.nba.com/" href="https://lakersgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/losangeles.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/losangeles.svg"><span class="team-name">Lakers Gaming</span></a></span>
                                        </td>
                                        <td>
                                            7.9
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>93</td>
                                        <td>
                                            <a ng-href="/player/natekahl/" href="/player/natekahl/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600077.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600077.png">
                                                </div>
                                                <div class="player-handle">
                                                    NateKahl
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://knicksgaming.nba.com/" href="https://knicksgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/new-york.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/new-york.svg"><span class="team-name">Knicks Gaming</span></a></span>
                                        </td>
                                        <td>
                                            7.8
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>94</td>
                                        <td>
                                            <a ng-href="/player/bulleyy/" href="/player/bulleyy/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600232.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600232.png">
                                                </div>
                                                <div class="player-handle">
                                                    Bulleyy
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://celticscrossover.nba.com/" href="https://celticscrossover.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/boston.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/boston.svg"><span class="team-name">Celtics Crossover Gaming</span></a></span>
                                        </td>
                                        <td>
                                            7.6
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>95</td>
                                        <td>
                                            <a ng-href="/player/crown/" href="/player/crown/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630409.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    Crown
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://hornetsvenomgt.nba.com/" href="https://hornetsvenomgt.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/charlotte.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/charlotte.svg"><span class="team-name">Hornets Venom GT</span></a></span>
                                        </td>
                                        <td>
                                            7.6
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>96</td>
                                        <td>
                                            <a ng-href="/player/yeah-i-compete/" href="/player/yeah-i-compete/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600037.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600037.png">
                                                </div>
                                                <div class="player-handle">
                                                    Yeah I Compete
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://jazzgaming.nba.com/" href="https://jazzgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/utah.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/utah.svg"><span class="team-name">Jazz Gaming</span></a></span>
                                        </td>
                                        <td>
                                            7.6
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>97</td>
                                        <td>
                                            <a ng-href="/player/steez/" href="/player/steez/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600003.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600003.png">
                                                </div>
                                                <div class="player-handle">
                                                    Steez
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://76ersgc.nba.com/" href="https://76ersgc.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/philadelphia.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/philadelphia.svg"><span class="team-name">76ers GC</span></a></span>
                                        </td>
                                        <td>
                                            7.6
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>98</td>
                                        <td>
                                            <a ng-href="/player/komp/" href="/player/komp/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630418.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    Komp
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://bucksgaming.nba.com/" href="https://bucksgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/milwaukee.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/milwaukee.svg"><span class="team-name">Bucks Gaming</span></a></span>
                                        </td>
                                        <td>
                                            7.5
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>99</td>
                                        <td>
                                            <a ng-href="/player/kayaus/" href="/player/kayaus/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630411.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    KayAus
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://warriorsgs.nba.com/" href="https://warriorsgs.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/golden-state.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/golden-state.svg"><span class="team-name">Warriors Gaming Squad</span></a></span>
                                        </td>
                                        <td>
                                            7.5
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>100</td>
                                        <td>
                                            <a ng-href="/player/tbshiftay/" href="/player/tbshiftay/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630058.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    TBShiftay
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://heatcheck.nba.com/" href="https://heatcheck.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/miami.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/miami.svg"><span class="team-name">Heat Check Gaming</span></a></span>
                                        </td>
                                        <td>
                                            7.4
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>101</td>
                                        <td>
                                            <a ng-href="/player/fakiee/" href="/player/fakiee/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630417.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630417.png">
                                                </div>
                                                <div class="player-handle">
                                                    Fakiee
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://hawkstalon.nba.com/" href="https://hawkstalon.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/atlanta.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/atlanta.svg"><span class="team-name">Hawks Talon GC</span></a></span>
                                        </td>
                                        <td>
                                            7.4
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>102</td>
                                        <td>
                                            <a ng-href="/player/just-awkward/" href="/player/just-awkward/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630073.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    Just Awkward
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://wizardsdg.nba.com/" href="https://wizardsdg.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/washington.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/washington.svg"><span class="team-name">Wizards District Gaming</span></a></span>
                                        </td>
                                        <td>
                                            7.4
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>103</td>
                                        <td>
                                            <a ng-href="/player/randomz/" href="/player/randomz/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630072.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    Randomz
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://blazer5gaming.nba.com/" href="https://blazer5gaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/portland.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/portland.svg"><span class="team-name">Blazer5 Gaming</span></a></span>
                                        </td>
                                        <td>
                                            7.3
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>104</td>
                                        <td>
                                            <a ng-href="/player/goddof2k/" href="/player/goddof2k/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600070.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600070.png">
                                                </div>
                                                <div class="player-handle">
                                                    Goddof2k
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://cavslegion.nba.com/" href="https://cavslegion.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/cleveland.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/cleveland.svg"><span class="team-name">Cavs Legion GC</span></a></span>
                                        </td>
                                        <td>
                                            7.1
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>105</td>
                                        <td>
                                            <a ng-href="/player/milo/" href="/player/milo/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630434.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    Milo
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://pistonsgt.nba.com/" href="https://pistonsgt.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/detroit.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/detroit.svg"><span class="team-name">Pistons GT</span></a></span>
                                        </td>
                                        <td>
                                            7.1
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>106</td>
                                        <td>
                                            <a ng-href="/player/timelycook/" href="/player/timelycook/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600063.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600063.png">
                                                </div>
                                                <div class="player-handle">
                                                    Timelycook
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://raptorsuprising.nba.com/" href="https://raptorsuprising.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/toronto.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/toronto.svg"><span class="team-name">Raptors Uprising GC</span></a></span>
                                        </td>
                                        <td>
                                            7.0
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>107</td>
                                        <td>
                                            <a ng-href="/player/bxmpydon/" href="/player/bxmpydon/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630422.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    BxmpyDon
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://gengtigers.nba.com/" href="https://gengtigers.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/shanghai.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/shanghai.svg"><span class="team-name">Gen.G Tigers</span></a></span>
                                        </td>
                                        <td>
                                            6.9
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>108</td>
                                        <td>
                                            <a ng-href="/player/turnupdefense/" href="/player/turnupdefense/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600054.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600054.png">
                                                </div>
                                                <div class="player-handle">
                                                    TURNUPDEFENSE
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://gengtigers.nba.com/" href="https://gengtigers.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/shanghai.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/shanghai.svg"><span class="team-name">Gen.G Tigers</span></a></span>
                                        </td>
                                        <td>
                                            6.8
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>109</td>
                                        <td>
                                            <a ng-href="/player/followthegod/" href="/player/followthegod/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630082.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    followTHEGOD
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://grizzgaming.nba.com/" href="https://grizzgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/memphis.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/memphis.svg"><span class="team-name">Grizz Gaming</span></a></span>
                                        </td>
                                        <td>
                                            6.7
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>110</td>
                                        <td>
                                            <a ng-href="/player/pexile/" href="/player/pexile/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630426.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    Pexile
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://pistonsgt.nba.com/" href="https://pistonsgt.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/detroit.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/detroit.svg"><span class="team-name">Pistons GT</span></a></span>
                                        </td>
                                        <td>
                                            6.6
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>111</td>
                                        <td>
                                            <a ng-href="/player/swann/" href="/player/swann/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630424.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630424.png">
                                                </div>
                                                <div class="player-handle">
                                                    Swann
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://hawkstalon.nba.com/" href="https://hawkstalon.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/atlanta.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/atlanta.svg"><span class="team-name">Hawks Talon GC</span></a></span>
                                        </td>
                                        <td>
                                            6.5
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>112</td>
                                        <td>
                                            <a ng-href="/player/deedz/" href="/player/deedz/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600058.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600058.png">
                                                </div>
                                                <div class="player-handle">
                                                    Deedz
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://heatcheck.nba.com/" href="https://heatcheck.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/miami.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/miami.svg"><span class="team-name">Heat Check Gaming</span></a></span>
                                        </td>
                                        <td>
                                            6.4
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>113</td>
                                        <td>
                                            <a ng-href="/player/tayzo/" href="/player/tayzo/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630401.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    TayZo
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://celticscrossover.nba.com/" href="https://celticscrossover.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/boston.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/boston.svg"><span class="team-name">Celtics Crossover Gaming</span></a></span>
                                        </td>
                                        <td>
                                            6.3
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>114</td>
                                        <td>
                                            <a ng-href="/player/nolovezar/" href="/player/nolovezar/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630405.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    NoLoveZar
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://knicksgaming.nba.com/" href="https://knicksgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/new-york.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/new-york.svg"><span class="team-name">Knicks Gaming</span></a></span>
                                        </td>
                                        <td>
                                            6.3
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>115</td>
                                        <td>
                                            <a ng-href="/player/bigrim/" href="/player/bigrim/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630068.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    BigRiM
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://cavslegion.nba.com/" href="https://cavslegion.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/cleveland.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/cleveland.svg"><span class="team-name">Cavs Legion GC</span></a></span>
                                        </td>
                                        <td>
                                            5.6
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>116</td>
                                        <td>
                                            <a ng-href="/player/underratedgoat/" href="/player/underratedgoat/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1630420.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png">
                                                </div>
                                                <div class="player-handle">
                                                    UnderRatedGoat
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://76ersgc.nba.com/" href="https://76ersgc.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/philadelphia.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/philadelphia.svg"><span class="team-name">76ers GC</span></a></span>
                                        </td>
                                        <td>
                                            5.3
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl --><tr data-ng-repeat="player in lls.pl">
                                        <td>117</td>
                                        <td>
                                            <a ng-href="/player/mrstylez/" href="/player/mrstylez/">
                                                <div class="player-headshot">
                                                    <img class="player-headshot__image" ng-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600248.png" on-error-src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/player-silo.png" src="https://ak-static.cms.nba.com/wp-content/uploads/headshots/2kleague/1600248.png">
                                                </div>
                                                <div class="player-handle">
                                                    MrStylez
                                                </div>
                                            </a>
                                        </td>
                                        <td>
                                            <span class="player-info__team"><a ng-href="https://mavsgaming.nba.com/" href="https://mavsgaming.nba.com/"><img ng-src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/dallas.svg" src="https://ak-static.cms.nba.com/wp-content/themes/nba-2k-parent/img/logos/dallas.svg"><span class="team-name">Mavs Gaming</span></a></span>
                                        </td>
                                        <td>
                                            4.6
                                            
                                            
                                            
                                            
                                            <span ng-show="player.fgp" class="ng-hide">%</span>
                                            <span ng-show="player.tpp" class="ng-hide">%</span>
                                            <span ng-show="player.ftp" class="ng-hide">%</span>
                                        </td>
                                    </tr><!-- end ngRepeat: player in lls.pl -->
                                </tbody>
                            </table>
                        </div><!-- end ngIf: lls.pl.length > 0 -->
                    </div>

                </div>

# Sidebar - Team selection
sorted_unique_team = sorted(())
selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

# Sidebar - Position selection
unique_pos = ['C','PF','SF','PG','SG']
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

# Filtering data
df_selected_team = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.Pos.isin(selected_pos))]

st.header('Display Player Stats of Selected Team(s)')
st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')
st.dataframe(df_selected_team)

# Download NBA player stats data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)

