/* @flow */

export type ZenObject = {
  id: number,
  value: string
}

export type ZenStateObject = {
  current = ?number,
  fetching = boolean,
  zens = Array<ZenObject>,
  saved = Array<number>
}
