import React from 'react'
import { Select } from 'react-materialize';
import './Categories.css'

export default () => (
  <Select
  id="Select-9"
  multiple={false}
  onChange={function noRefCheck(){}}
  options={{
    classes: '',
    dropdownOptions: {
      alignment: 'left',
      autoTrigger: true,
      closeOnClick: true,
      constrainWidth: true,
      coverTrigger: true,
      hover: false,
      inDuration: 150,
      onCloseEnd: null,
      onCloseStart: null,
      onOpenEnd: null,
      onOpenStart: null,
      outDuration: 250
    }
  }}
  value=""
>
  <option
    disabled
    value=""
  >
    Choose Category
  </option>
  <option value="1">
    flowers
  </option>
  <option value="2">
    Wood
  </option>
  <option value="3">
    Fruit
  </option>
  <option value="4">
    Other
  </option>
  <option value="5">
    Beverages
  </option>
</Select>
)