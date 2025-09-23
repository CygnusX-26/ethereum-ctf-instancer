// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

contract Setup {

    constructor() payable {
        // Any contract initialization here. This constructor will be called with 100 ETH.
    }

    function isSolved() public view returns (bool solved) {
        solved = true;
    }
}