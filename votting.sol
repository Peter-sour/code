// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Voting {
    struct Candidate {
        string name;
        uint voteCount;
    }

    address public owner;
    Candidate[] public candidates;
    uint public endTime;

    constructor(uint durationMinutes) {
        owner = msg.sender;
        endTime = block.timestamp + durationMinutes * 1 minutes;
    }
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can add candidates");
        _;
    }

    modifier votingOpen() {
        require(block.timestamp < endTime, "Voting has ended");
        _;
    }

    function addCandidate(string memory name) public onlyOwner {
        candidates.push(Candidate(name, 0));
    }

    function vote(uint candidateIndex) public votingOpen {
        require(candidateIndex < candidates.length, "Invalid candidate");
        candidates[candidateIndex].voteCount += 1;
    }

    function getWinner() public view returns (string memory) {
        uint winningVoteCount = 0;
        string memory winnerName;
        for (uint i = 0; i < candidates.length; i++) {
            if (candidates[i].voteCount > winningVoteCount) {
                winningVoteCount = candidates[i].voteCount;
                winnerName = candidates[i].name;
            }
        }
        return winnerName;
    }
}
