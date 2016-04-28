angular.module('visualFirewallModule')
    .factory('visualFirewallService', () => {

        var api = {
            setSpeed: setSpeed,
            addWhiteList: addWhiteList,
            getSpeed: getSpeed,
            getWhitelist: getWhitelist,
            speed: null,
            whiteList: []
        }

        function setSpeed(userSpeed) {
            api.speed = userSpeed;
        }

        function addWhiteList(whitelistIP) {
            api.whiteList.push(whitelistIP);
        }

        function getSpeed() {
            return speed;
        }

        function getWhitelist()
        {
            return whiteList;
        }

    });